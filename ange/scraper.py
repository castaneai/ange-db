# -*- coding: utf-8 -*-
from pyquery import PyQuery


def get_card(card_id, html_file):
    with open(html_file, encoding='cp932') as f:
        raw = f.read()
        html = PyQuery(raw)

    html_parameters = html('#detail_card_params .paramTable')
    html_profile = html('#scene_main')
    if len(html_profile) < 1:
        return None

    return {
        'id': card_id,
        'image_url': {
            'icon': 'http://img.sega-net.com/ange/resource/card/card_{0}1_s.png'.format(card_id),
            'card': 'http://img.sega-net.com/ange/resource/card/card_{0}1_l.jpg'.format(card_id),
            'character': 'http://img.sega-net.com/ange/resource/progress/progress_{0}_l.png'.format(card_id)
        },
        'name': html('#detail_card_name_inner').text(),
        'rarity': html('#detail_card_rare').text(),
        'world': html('#world_name span:first').text(),
        'max_lv': int(html('#world_name .lvWrap .fontBlue').text()),
        'parameters': {
            'power': int(html_parameters.find('tr').eq(0).find('td').eq(0).find('.fontBlue').text()),
            'guard': int(html_parameters.find('tr').eq(0).find('td').eq(1).find('.fontBlue').text()),
            'speed': int(html_parameters.find('tr').eq(1).find('td').eq(0).find('.fontBlue').text()),
            'cost': int(html_parameters('tr').eq(1).find('td').eq(1).find('.fontBlue').text()),
        },
        'profile': {
            'description': html_profile('.charaInfo').text(),
            'likes': html_profile('.prof li').eq(0).find('span').text().split('、'),
            'dislikes': html_profile('.prof li').eq(1).find('span').text().split('、'),
            'motto': html_profile('.prof li').eq(2).text(),
        },
        'creator': {
            'illust': html_profile('.creater li').eq(0).find('span').text().strip(),
            'voice': html_profile('.creater li').eq(1).find('span').text().strip(),
        }
    }


if __name__ == '__main__':
    card = get_card(1001, 'target.html')
    print(card)
