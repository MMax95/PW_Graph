# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.graph import Graph  # noqa: E501
from openapi_server.models.node import Node  # noqa: E501
from openapi_server.test import BaseTestCase


class TestGraphController(BaseTestCase):
    """GraphController integration test stubs"""

    @unittest.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
    def test_add_custom_graph(self):
        """Test case for add_custom_graph

        Add a new custom graph
        """
        body = {
  "relations" : [ {
    "internalParameters" : [ {
      "parameterType" : "integer",
      "parameterID" : 6,
      "parameterName" : "parameterName",
      "parameterValue" : "parameterValue"
    }, {
      "parameterType" : "integer",
      "parameterID" : 6,
      "parameterName" : "parameterName",
      "parameterValue" : "parameterValue"
    } ],
    "relationID" : 6,
    "triggers" : [ {
      "targetParameterID" : 5,
      "triggerType" : "biggerThanTarget",
      "sourceParameterID" : 1
    }, {
      "targetParameterID" : 5,
      "triggerType" : "biggerThanTarget",
      "sourceParameterID" : 1
    } ],
    "actions" : [ {
      "actionType" : "modifyTarget",
      "targetParameterID" : 2,
      "sourceParameterID" : 5
    }, {
      "actionType" : "modifyTarget",
      "targetParameterID" : 2,
      "sourceParameterID" : 5
    } ]
  }, {
    "internalParameters" : [ {
      "parameterType" : "integer",
      "parameterID" : 6,
      "parameterName" : "parameterName",
      "parameterValue" : "parameterValue"
    }, {
      "parameterType" : "integer",
      "parameterID" : 6,
      "parameterName" : "parameterName",
      "parameterValue" : "parameterValue"
    } ],
    "relationID" : 6,
    "triggers" : [ {
      "targetParameterID" : 5,
      "triggerType" : "biggerThanTarget",
      "sourceParameterID" : 1
    }, {
      "targetParameterID" : 5,
      "triggerType" : "biggerThanTarget",
      "sourceParameterID" : 1
    } ],
    "actions" : [ {
      "actionType" : "modifyTarget",
      "targetParameterID" : 2,
      "sourceParameterID" : 5
    }, {
      "actionType" : "modifyTarget",
      "targetParameterID" : 2,
      "sourceParameterID" : 5
    } ]
  } ],
  "nodeID" : 0,
  "parameters" : [ {
    "parameterType" : "integer",
    "parameterID" : 6,
    "parameterName" : "parameterName",
    "parameterValue" : "parameterValue"
  }, {
    "parameterType" : "integer",
    "parameterID" : 6,
    "parameterName" : "parameterName",
    "parameterValue" : "parameterValue"
  } ],
  "status" : "Pending"
}
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v2/graphs',
            method='POST',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("application/x-www-form-urlencoded not supported by Connexion")
    def test_add_filter_view(self):
        """Test case for add_filter_view

        Edit graph filter view
        """
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded',
            'api_key': 'special-key',
            'Authorization': 'Bearer special-key',
        }
        data = dict(view_index=56,
                    target_parameter='target_parameter_example')
        response = self.client.open(
            '/v2/graphs/{graph_id}'.format(graph_id=56),
            method='POST',
            headers=headers,
            data=data,
            content_type='application/x-www-form-urlencoded')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("application/x-www-form-urlencoded not supported by Connexion")
    def test_add_graph_parameter(self):
        """Test case for add_graph_parameter

        Adds a new global parameter to the graph
        """
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded',
            'api_key': 'special-key',
        }
        data = dict(name='name_example',
                    parameter_type='parameter_type_example',
                    parameter_value='parameter_value_example')
        response = self.client.open(
            '/v2/graphs/{graph_id}'.format(graph_id=56),
            method='PUT',
            headers=headers,
            data=data,
            content_type='application/x-www-form-urlencoded')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
    def test_add_template_graph(self):
        """Test case for add_template_graph

        Add a new template graph
        """
        body = {
  "defaultView" : 5,
  "graphID" : 0,
  "parameters" : [ {
    "parameterType" : "integer",
    "parameterID" : 6,
    "parameterName" : "parameterName",
    "parameterValue" : "parameterValue"
  }, {
    "parameterType" : "integer",
    "parameterID" : 6,
    "parameterName" : "parameterName",
    "parameterValue" : "parameterValue"
  } ],
  "views" : [ {
    "viewID" : 1,
    "filterParameters" : [ {
      "parameterType" : "integer",
      "parameterID" : 6,
      "parameterName" : "parameterName",
      "parameterValue" : "parameterValue"
    }, {
      "parameterType" : "integer",
      "parameterID" : 6,
      "parameterName" : "parameterName",
      "parameterValue" : "parameterValue"
    } ]
  }, {
    "viewID" : 1,
    "filterParameters" : [ {
      "parameterType" : "integer",
      "parameterID" : 6,
      "parameterName" : "parameterName",
      "parameterValue" : "parameterValue"
    }, {
      "parameterType" : "integer",
      "parameterID" : 6,
      "parameterName" : "parameterName",
      "parameterValue" : "parameterValue"
    } ]
  } ]
}
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v2/graphs',
            method='PUT',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_graph(self):
        """Test case for delete_graph

        Deletes a graph
        """
        headers = { 
            'api_key': 'api_key_example',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v2/graphs/{graph_id}'.format(graph_id=56),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("application/x-www-form-urlencoded not supported by Connexion")
    def test_edit_graph_parameter(self):
        """Test case for edit_graph_parameter

        Updates a global parameter
        """
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded',
            'api_key': 'special-key',
        }
        data = dict(name='name_example',
                    parameter_value='parameter_value_example')
        response = self.client.open(
            '/v2/graphs/{graph_id}'.format(graph_id=56),
            method='PATCH',
            headers=headers,
            data=data,
            content_type='application/x-www-form-urlencoded')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_graph_by_id(self):
        """Test case for get_graph_by_id

        Find graph by ID
        """
        headers = { 
            'Accept': 'application/json',
            'api_key': 'special-key',
        }
        response = self.client.open(
            '/v2/graphs/{graph_id}'.format(graph_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_graphs_get(self):
        """Test case for graphs_get

        Show user's graphs
        """
        headers = { 
        }
        response = self.client.open(
            '/v2/graphs',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
