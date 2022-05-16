import connexion
import six

from openapi_server.models.node import Node  # noqa: E501
from openapi_server import util


def add_custom_node(body):  # noqa: E501
    """Add a custom node to the graph

     # noqa: E501

    :param body: Node object that needs to be added to the network
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Node.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def add_node_parameter(node_id, name, parameter_type, parameter_value):  # noqa: E501
    """Adds a new parameter to the node

     # noqa: E501

    :param node_id: ID of the node that needs to be updated
    :type node_id: int
    :param name: The name of the added parameter
    :type name: str
    :param parameter_type: The type of parameter added to the node
    :type parameter_type: str
    :param parameter_value: The value of the parameter added to the node
    :type parameter_value: str

    :rtype: Node
    """
    return 'do some magic!'


def add_node_trigger(node_id, target_parameter, trigger_type, trigger_index=None, target_node_id=None):  # noqa: E501
    """Add node trigger

     # noqa: E501

    :param node_id: ID of the node that needs to be updated
    :type node_id: int
    :param target_parameter: Name of the target trigger parameter
    :type target_parameter: str
    :param trigger_type: The type of trigger condition
    :type trigger_type: str
    :param trigger_index: If provided, specifies the trigger to be replaced
    :type trigger_index: int
    :param target_node_id: The ID of the target node. If not provided, global graph variables will be used
    :type target_node_id: int

    :rtype: Node
    """
    return 'do some magic!'


def add_template_node(body):  # noqa: E501
    """Add template node to the graph

     # noqa: E501

    :param body: Node object that needs to be added to the network
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Node.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_node(node_id, api_key=None):  # noqa: E501
    """Deletes a node

     # noqa: E501

    :param node_id: Node ID to delete
    :type node_id: int
    :param api_key: 
    :type api_key: str

    :rtype: None
    """
    return 'do some magic!'


def edit_node_parameter(node_id, name, parameter_value=None):  # noqa: E501
    """Updates a node parameter

     # noqa: E501

    :param node_id: ID of the node that needs to be updated
    :type node_id: int
    :param name: The name of the modified parameter
    :type name: str
    :param parameter_value: The value of the edited parameter. If not provided, the parameter is deleted
    :type parameter_value: str

    :rtype: Node
    """
    return 'do some magic!'


def find_nodes_by_status(status):  # noqa: E501
    """Finds node by status

    Multiple status values can be provided with comma separated strings # noqa: E501

    :param status: Status values that need to be considered for filter
    :type status: List[str]

    :rtype: List[Node]
    """
    return 'do some magic!'


def get_node_by_id(node_id):  # noqa: E501
    """Find node by ID

    Returns a single node # noqa: E501

    :param node_id: ID of node to return
    :type node_id: int

    :rtype: Node
    """
    return 'do some magic!'


def nodes_get():  # noqa: E501
    """Show nodes in the selected graph

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'
