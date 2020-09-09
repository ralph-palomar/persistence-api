# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_modify_id_put(self):
        """Test case for modify_id_put

        
        """
        query_string = [('collection', 'collection_example')]
        response = self.client.open(
            '/public/api/v1/persistence/modify/{id}'.format(id='id_example'),
            method='PUT',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_remove_id_get(self):
        """Test case for remove_id_get

        
        """
        query_string = [('collection', 'collection_example')]
        response = self.client.open(
            '/public/api/v1/persistence/remove/{id}'.format(id='id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_get(self):
        """Test case for retrieve_get

        
        """
        query_string = [('collection', 'collection_example')]
        response = self.client.open(
            '/public/api/v1/persistence/retrieve',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_id_get(self):
        """Test case for retrieve_id_get

        
        """
        query_string = [('collection', 'collection_example')]
        response = self.client.open(
            '/public/api/v1/persistence/retrieve/{id}'.format(id='id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_save_post(self):
        """Test case for save_post

        
        """
        body = None
        query_string = [('collection', 'collection_example')]
        response = self.client.open(
            '/public/api/v1/persistence/save',
            method='POST',
            data=json.dumps(body),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
