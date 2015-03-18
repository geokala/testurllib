#! /usr/bin/env python
import urllib
import urllib2


def call_local_url(path, post=False, post_data={}):
    if post:
        response = urllib2.urlopen(
            'http://127.0.0.1/{path}'.format(path=path),
            urllib.urlencode(post_data),
            )
    else:
        response = urllib2.urlopen(
            'http://127.0.0.1/{path}'.format(path=path)
            )
    data = response.read()
    return data


if __name__ == '__main__':
    print(call_local_url(path=''))
    print('===========')
    print(call_local_url(path='', post=True, post_data={'test': 1}))
