# -*- coding: utf-8 -*-
from bottle import route, template, run
import card


@route('/')
def index():
    cards = [card.get_card(1001, 'target.html')]
    return template('index', cards=cards)


run(host='localhost', port=7777, debug=True)