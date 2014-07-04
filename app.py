# -*- coding: utf-8 -*-
import os.path
from bottle import route, request, template, run, static_file
import ange.db


def static_cache(filepath, create_func):
    if not os.path.exists(filepath):
        data = create_func()
        with open(filepath, 'wb') as f:
            f.write(data)
    return static_file(filepath, root='./')


@route('/')
def index():
    keyword = request.query.keyword or None
    cards = ange.db.search(keyword)
    return template('index', cards=cards)


@route('/images/icon/<card_id>.png')
def icon(card_id):
    cache_path = './public/images/icon/{0}.png'.format(card_id)
    return static_cache(cache_path, lambda: ange.db.get_icon_image(card_id))


@route('/images/character/<card_id>.png')
def icon(card_id):
    cache_path = './public/images/character/{0}.png'.format(card_id)
    return static_cache(cache_path, lambda: ange.db.get_character_image(card_id))

@route('/<filepath:path>')
def static(filepath):
    return static_file(filepath, root='./public')


run(host='127.0.0.1', port=7777, debug=False)