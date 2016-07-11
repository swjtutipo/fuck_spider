# coding=utf-8
# __author__ = tipo
# __create__ = 16/6/4 下午5:10

import logging
import time
import requests

logger = logging.getLogger(__name__)


class Request(object):
    """
    request by http
    """
    @classmethod
    def request(cls, method, url, params=None, data=None, headers=None, timeout=3):
        """
        params: query param
        data: form data
        """
        response = None
        try:
            s_time = time.time()
            if method == 'GET':
                response = requests.get(
                    url,
                    params=params,
                    headers=headers,
                    timeout=timeout
                )
            elif method == 'POST':
                response = requests.post(
                    url,
                    data=data,
                    params=params,
                    headers=headers,
                    timeout=timeout
                )
            logger.info('[RESPONSE TIME] url [{}], response time [{}]'.format(
                url, time.time() - s_time
            ))
            return response.text
        except Exception as e:
            logger.error(
                '[REQUEST ERROR] message [{}], method [{}], '
                'url [{}], params [{}], data [{}] headers [{}]'.format(
                    e, method, url, params, data, headers
                )
            )

        return response

if __name__ == '__main__':
    url = 'http://www.baidu.com'
    result = Request.request('GET', url)
    print result
