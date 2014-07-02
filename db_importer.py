# -*- coding: utf-8 -*-
import ange.scraper
import ange.db
import glob
import os.path


def get_available_cards():
    for html_file in glob.glob('./_crawled/*.html'):
        card_id = int(os.path.basename(html_file).split('.')[0])
        card = ange.scraper.get_card(card_id, html_file)
        if card is not None:
            yield card

if __name__ == '__main__':
    ange.db.create_table()
    ange.db.add_all(get_available_cards())
