# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.node import Node  # noqa: E501
from openapi_server.test import BaseTestCase


class TestNodeController(BaseTestCase):
    """NodeController integration test stubs"""

    @unittest.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
    def test_add_custom_node(self):
        """Test case for add_custom_node

        Add a custom node to the graph
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
            '/v2/nodes',
            method='POST',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("application/x-www-form-urlencoded not supported by Connexion")
    def test_add_node_parameter(self):
        """Test case for add_node_parameter

        Adds a new parameter to the node
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
            '/v2/nodes/{node_id}'.format(node_id=56),
            method='PUT',
            headers=headers,
            data=data,
            content_type='application/x-www-form-urlencoded')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("application/x-www-form-urlencoded not supported by Connexion")
    def test_add_node_trigger(self):
        """Test case for add_node_trigger

        Add node trigger
        """
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded',
            'api_key': 'special-key',
            'Authorization': 'Bearer special-key',
        }
        data = dict(trigger_index=56,
                    target_node_id=56,
                    target_parameter='target_parameter_example',
                    trigger_type='trigger_type_example')
        response = self.client.open(
            '/v2/nodes/{node_id}'.format(node_id=56),
            method='POST',
            headers=headers,
            data=data,
            content_type='application/x-www-form-urlencoded')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
    def test_add_template_node(self):
        """Test case for add_template_node

        Add template node to the graph
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
            '/v2/nodes',
            method='PUT',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_node(self):
        """Test case for delete_node

        Deletes a node
        """
        headers = { 
            'api_key': 'api_key_example',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v2/nodes/{node_id}'.format(node_id=56),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("application/x-www-form-urlencoded not supported by Connexion")
    def test_edit_node_parameter(self):
        """Test case for edit_node_parameter

        Updates a node parameter
        """
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded',
            'api_key': 'special-key',
        }
        data = dict(name='name_example',
                    parameter_value='parameter_value_example')
        response = self.client.open(
            '/v2/nodes/{node_id}'.format(node_id=56),
            method='PATCH',
            headers=headers,
            data=data,
            content_type='application/x-www-form-urlencoded')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_nodes_by_status(self):
        """Test case for find_nodes_by_status

        Finds node by status
        """
        query_string = [('status', ['status_example'])]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v2/node/findByStatus',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_node_by_id(self):
        """Test case for get_node_by_id

        Find node by ID
        """
        headers = { 
            'Accept': 'application/json',
            'api_key': 'special-key',
        }
        response = self.client.open(
            '/v2/nodes/{node_id}'.format(node_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_nodes_get(self):
        """Test case for nodes_get

        Show nodes in the selected graph
        """
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v2/nodes',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
