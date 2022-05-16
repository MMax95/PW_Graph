# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Trigger(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, trigger_type=None, source_parameter_id=None, target_parameter_id=None):  # noqa: E501
        """Trigger - a model defined in OpenAPI

        :param trigger_type: The trigger_type of this Trigger.  # noqa: E501
        :type trigger_type: str
        :param source_parameter_id: The source_parameter_id of this Trigger.  # noqa: E501
        :type source_parameter_id: int
        :param target_parameter_id: The target_parameter_id of this Trigger.  # noqa: E501
        :type target_parameter_id: int
        """
        self.openapi_types = {
            'trigger_type': str,
            'source_parameter_id': int,
            'target_parameter_id': int
        }

        self.attribute_map = {
            'trigger_type': 'triggerType',
            'source_parameter_id': 'sourceParameterID',
            'target_parameter_id': 'targetParameterID'
        }

        self._trigger_type = trigger_type
        self._source_parameter_id = source_parameter_id
        self._target_parameter_id = target_parameter_id

    @classmethod
    def from_dict(cls, dikt) -> 'Trigger':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Trigger of this Trigger.  # noqa: E501
        :rtype: Trigger
        """
        return util.deserialize_model(dikt, cls)

    @property
    def trigger_type(self):
        """Gets the trigger_type of this Trigger.

        Trigger type  # noqa: E501

        :return: The trigger_type of this Trigger.
        :rtype: str
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        """Sets the trigger_type of this Trigger.

        Trigger type  # noqa: E501

        :param trigger_type: The trigger_type of this Trigger.
        :type trigger_type: str
        """
        allowed_values = ["biggerThanTarget", "smallerThanTarget", "equalToTarget", "betweenSources", "matchTargetToList"]  # noqa: E501
        if trigger_type not in allowed_values:
            raise ValueError(
                "Invalid value for `trigger_type` ({0}), must be one of {1}"
                .format(trigger_type, allowed_values)
            )

        self._trigger_type = trigger_type

    @property
    def source_parameter_id(self):
        """Gets the source_parameter_id of this Trigger.


        :return: The source_parameter_id of this Trigger.
        :rtype: int
        """
        return self._source_parameter_id

    @source_parameter_id.setter
    def source_parameter_id(self, source_parameter_id):
        """Sets the source_parameter_id of this Trigger.


        :param source_parameter_id: The source_parameter_id of this Trigger.
        :type source_parameter_id: int
        """
        if source_parameter_id is None:
            raise ValueError("Invalid value for `source_parameter_id`, must not be `None`")  # noqa: E501

        self._source_parameter_id = source_parameter_id

    @property
    def target_parameter_id(self):
        """Gets the target_parameter_id of this Trigger.


        :return: The target_parameter_id of this Trigger.
        :rtype: int
        """
        return self._target_parameter_id

    @target_parameter_id.setter
    def target_parameter_id(self, target_parameter_id):
        """Sets the target_parameter_id of this Trigger.


        :param target_parameter_id: The target_parameter_id of this Trigger.
        :type target_parameter_id: int
        """
        if target_parameter_id is None:
            raise ValueError("Invalid value for `target_parameter_id`, must not be `None`")  # noqa: E501

        self._target_parameter_id = target_parameter_id
