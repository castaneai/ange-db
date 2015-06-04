# -*- coding: utf-8 -*-
import os
import os.path
from bottle import route, request, template, run, static_file
import ange.db


def static_cache(filepath, create_data_func):
    if not os.path.exists(filepath):
        with open(filepath, 'wb') as f:
            f.write(create_data_func())
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

# create image cache dirs
dirs = ['/public/images/icon', '/public/images/character']
for d in dirs:
    os.makedirs(os.path.abspath(os.path.dirname(__file__)) + d, exist_ok=True)
run(host='127.0.0.1', port=7777, debug=False)
