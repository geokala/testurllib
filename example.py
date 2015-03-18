#! /usr/bin/env python
import urllib
import urllib2


def call_local_url(path, post=False, post_data={}, headers={}):
    if post:
        request = urllib2.Request(
            'http://127.0.0.1/{path}'.format(path=path),
            urllib.urlencode(post_data),
            headers=headers,
            )
    else:
        request = urllib2.Request(
            'http://127.0.0.1/{path}'.format(path=path),
            headers=headers,
            )
    response = urllib2.urlopen(request)
    data = response.read()
    return data


if __name__ == '__main__':
    print(call_local_url(path=''))
    print('===========')
    print(call_local_url(path='', post=True, post_data={'test': 1}))
    print('===========')
    print(call_local_url(path='', headers={'User-Agent': 'woogle'}))
    print('===========')
    print(call_local_url(path='', post=True, post_data={'test': 1},
                         headers={'User-Agent': 'wooglepost'}))
