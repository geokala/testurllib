import mock
import os
import sys
import unittest

# Allow the tests to work from a tests subdir, then import the test target
test_path = os.path.dirname(__file__)
sys.path.append(os.path.split(test_path)[0])

# Module to be tested
import example


class TestUrlCalls(unittest.TestCase):
    def setUp(self):
        self.oldrequest = example.urllib2.Request
        self.oldopen = example.urllib2.urlopen

        example.urllib2.Request = mock.Mock()
        example.urllib2.urlopen = mock.Mock()

    def tearDown(self):
        example.urllib2.Request = self.oldrequest
        example.urllib2.urlopen = self.oldopen

    def test_get(self):
        example.call_local_url('')
        example.urllib2.Request.assert_called_with(
            'http://127.0.0.1/',
            headers={},
        )

    def test_post(self):
        example.call_local_url('', post=True)
        example.urllib2.Request.assert_called_with(
            'http://127.0.0.1/',
            '',
            headers={},
        )

    def test_post_params(self):
        example.call_local_url('', post=True, post_data={'hello': 'yes'})
        example.urllib2.Request.asser_called_with(
            'http://127.0.0.1/',
            'hello=yes',
            headers={},
        )

    def test_custom_headers(self):
        example.call_local_url('', post=True, headers={'munge': 'true'})
        example.urllib2.Request.assert_called_with(
            'http://127.0.0.1/',
            '',
            headers={'munge': 'true'},
        )
