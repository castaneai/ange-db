# -*- coding: utf-8 -*-
import os.path
from bottle import route, request, template, run, static_file
import ange.db


@route('/')
def index():
    keyword = request.query.keyword or None
    cards = ange.db.search(keyword)
    return template('index', cards=cards)


@route('/images/icon/<card_id>')
def icon(card_id):
    cache_path = './images/icon/{0}.png'.format(card_id)
    if not os.path.exists(cache_path):
        data = ange.db.get_icon_image(card_id)
        with open(cache_path, 'wb') as f:
            f.write(data)
    return static_file(cache_path, root='.')


@route('/images/character/<card_id>')
def icon(card_id):
    cache_path = './images/character/{0}.png'.format(card_id)
    if not os.path.exists(cache_path):
        data = ange.db.get_character_image(card_id)
        with open(cache_path, 'wb') as f:
            f.write(data)
    return static_file(cache_path, root='.')

run(host='0.0.0.0', port=10800, debug=False)