#! /usr/bin/env python
import urllib2


def get_local_url(path):
    response = urllib2.urlopen('http://127.0.0.1/{path}'.format(path=path))
    data = response.read()
    return data


if __name__ == '__main__':
    print(get_local_url(path=''))
