# coding=utf-8
# __author__ = tipo
# __create__ = 16/6/4 下午6:00

from multiprocessing import Process
import logging
import bs4
import hashlib
from common.request import Request

logger = logging.getLogger(__name__)
URL_POOL = [
    'http://www.meizitu.com'
]
PATH = '../../../Pictures'


def save_img(url):
    """
    save image
    """
    try:
        image = Request.request('GET', url)
        if image.content:
            with open('{}/{}.jpg'.format(PATH, hashlib.md5(url).hexdigest()), 'wb') as f:
                for chunk in image.iter_content(chunk_size=1024):
                    f.write(chunk)
    except Exception as e:
        logger.error('save image error, url [{}], error message [{}]'.format(url, e))


def parse_html(html):
    """
    parse html
    """
    process_list = []
    bs_data = bs4.BeautifulSoup(html)
    for img in bs_data.find_all('img'):
        process = Process(target=save_img, args=(img['src'],))
        process.start()
    for process in process_list:
        process.join()


def fetch(url):
    """
    fetch html
    """
    html = Request.request('GET', url).text
    parse_html(html)


def run():
    process_list = []
    for url in URL_POOL:
        process = Process(target=fetch, args=(url,))
        process.start()
        process_list.append(process)
    for process in process_list:
        process.join()


if __name__ == '__main__':
    run()
