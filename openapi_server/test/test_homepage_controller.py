# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.test import BaseTestCase


class TestHomepageController(BaseTestCase):
    """HomepageController integration test stubs"""

    def test_get_homepage(self):
        """Test case for get_homepage

        Show the homepage
        """
        headers = { 
            'Accept': 'text/html',
        }
        response = self.client.open(
            '/v2/',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
