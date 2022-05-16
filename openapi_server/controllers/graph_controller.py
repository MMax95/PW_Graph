import connexion
import six

from openapi_server.models.graph import Graph  # noqa: E501
from openapi_server.models.node import Node  # noqa: E501
from openapi_server import util


def add_custom_graph(body):  # noqa: E501
    """Add a new custom graph

     # noqa: E501

    :param body: Graph object hosting node network
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Node.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def add_filter_view(graph_id, view_index=None, target_parameter=None):  # noqa: E501
    """Edit graph filter view

     # noqa: E501

    :param graph_id: ID of the node that needs to be updated
    :type graph_id: int
    :param view_index: If provided, specifies the view to be replaced
    :type view_index: int
    :param target_parameter: Name of the target trigger parameter. If not provided, deletes the filtered view
    :type target_parameter: str

    :rtype: Node
    """
    return 'do some magic!'


def add_graph_parameter(graph_id, name, parameter_type, parameter_value):  # noqa: E501
    """Adds a new global parameter to the graph

     # noqa: E501

    :param graph_id: ID of the graph that needs to be updated
    :type graph_id: int
    :param name: The name of the added parameter
    :type name: str
    :param parameter_type: The type of parameter added to the node
    :type parameter_type: str
    :param parameter_value: The value of the parameter added to the node
    :type parameter_value: str

    :rtype: Node
    """
    return 'do some magic!'


def add_template_graph(body):  # noqa: E501
    """Add a new template graph

     # noqa: E501

    :param body: Graph object hosting node network
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Graph.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_graph(graph_id, api_key=None):  # noqa: E501
    """Deletes a graph

     # noqa: E501

    :param graph_id: Id of the graph to delete
    :type graph_id: int
    :param api_key: 
    :type api_key: str

    :rtype: None
    """
    return 'do some magic!'


def edit_graph_parameter(graph_id, name, parameter_value=None):  # noqa: E501
    """Updates a global parameter

     # noqa: E501

    :param graph_id: ID of the graph that needs to be updated
    :type graph_id: int
    :param name: The name of the modified parameter
    :type name: str
    :param parameter_value: The value of the edited parameter. If not provided, the parameter is deleted
    :type parameter_value: str

    :rtype: Node
    """
    return 'do some magic!'


def get_graph_by_id(graph_id):  # noqa: E501
    """Find graph by ID

    Returns a graph network # noqa: E501

    :param graph_id: ID of graph to return
    :type graph_id: int

    :rtype: Node
    """
    return 'do some magic!'


def graphs_get():  # noqa: E501
    """Show user&#39;s graphs

     # noqa: E501


    :rtype: None
    """
    return 'This *Should* return some graphs'
