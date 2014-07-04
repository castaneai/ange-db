# -*- coding: utf-8 -*-
import os.path
import sqlalchemy
import sqlalchemy.ext.declarative

_DB_PATH = os.path.join(os.path.dirname(__file__), '../cards.db')
_engine = sqlalchemy.create_engine('sqlite:///{0}'.format(_DB_PATH), echo=True)
_BaseTableClass = sqlalchemy.ext.declarative.declarative_base()


class CardSchema(_BaseTableClass):
    from sqlalchemy import Column, Integer, String, LargeBinary
    __tablename__ = 'cards'

    id = Column(Integer, primary_key=True)
    image_icon = Column(LargeBinary)
    image_character = Column(LargeBinary)
    name = Column(String)
    rarity = Column(String)
    world = Column(String)
    max_lv = Column(Integer)
    power = Column(Integer)
    guard = Column(Integer)
    speed = Column(Integer)
    cost = Column(Integer)
    description = Column(String)
    illustrator = Column(String)
    voice = Column(String)


def create_table():
    _BaseTableClass.metadata.create_all(_engine)


def create_new_session():
    import sqlalchemy.orm
    Session = sqlalchemy.orm.sessionmaker(bind=_engine)
    return Session()


def get_url_content(url):
    """指定したURLのファイルの中身を返す
    Content-Typeによってテキストからバイナリ化は自動判別されるらしい"""
    import urllib.request
    with urllib.request.urlopen(url) as f:
        return f.read()


def create_schema(card):
    return CardSchema(
        id=card['id'],
        image_icon=get_url_content(card['image_url']['icon']),
        image_character=get_url_content(card['image_url']['character']),
        name=card['name'],
        rarity=card['rarity'],
        world=card['world'],
        max_lv=card['max_lv'],
        power=card['parameters']['power'],
        guard=card['parameters']['guard'],
        speed=card['parameters']['speed'],
        cost=card['parameters']['cost'],
        description=card['profile']['description'],
        illustrator=card['creator']['illust'],
        voice=card['creator']['voice']
    )


def add(card):
    session = create_new_session()
    session.add(create_schema(card))
    session.commit()


def add_all(cards):
    session = create_new_session()
    session.add_all([create_schema(card) for card in cards])
    session.commit()


def search(keyword=None):
    session = create_new_session()
    query = session.query(CardSchema)
    if keyword:
        query = query.filter(sqlalchemy.or_(
            CardSchema.name.like('%{0}%'.format(keyword)),
            CardSchema.voice.like('%{0}%'.format(keyword)),
            CardSchema.illustrator.like('%{0}%'.format(keyword))
        ))
    return query.all()


def get_icon_image(card_id):
    session = create_new_session()
    query = session.query(CardSchema).filter_by(id=card_id)
    return query.one().image_icon


def get_character_image(card_id):
    session = create_new_session()
    query = session.query(CardSchema).filter_by(id=card_id)
    return query.one().image_character
