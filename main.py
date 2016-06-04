# coding=utf-8
# __author__ = tipo
# __create__ = 16/6/4 下午6:00

import logging
import bs4
from common.request import Request

logger = logging.getLogger(__name__)
URL_POOL = [
    'http://www.baidu.com'
]


def parse_html(html):
    """
    parse html
    """
    pass


def run():
    for url in URL_POOL:
        html = Request.request('GET', url)
        parse_html(html)


if __name__ == '__main__':
    run()
