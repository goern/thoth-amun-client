# coding: utf-8

"""
    Amun API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from amun.swagger_client.models.inspection_build_status_response_status import InspectionBuildStatusResponseStatus  # noqa: F401,E501


class InspectionBuildStatusResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'status': 'InspectionBuildStatusResponseStatus',
        'parameters': 'object'
    }

    attribute_map = {
        'status': 'status',
        'parameters': 'parameters'
    }

    def __init__(self, status=None, parameters=None):  # noqa: E501
        """InspectionBuildStatusResponse - a model defined in Swagger"""  # noqa: E501

        self._status = None
        self._parameters = None
        self.discriminator = None

        self.status = status
        self.parameters = parameters

    @property
    def status(self):
        """Gets the status of this InspectionBuildStatusResponse.  # noqa: E501


        :return: The status of this InspectionBuildStatusResponse.  # noqa: E501
        :rtype: InspectionBuildStatusResponseStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InspectionBuildStatusResponse.


        :param status: The status of this InspectionBuildStatusResponse.  # noqa: E501
        :type: InspectionBuildStatusResponseStatus
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def parameters(self):
        """Gets the parameters of this InspectionBuildStatusResponse.  # noqa: E501

        Parameters echoed back to user for debugging.  # noqa: E501

        :return: The parameters of this InspectionBuildStatusResponse.  # noqa: E501
        :rtype: object
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this InspectionBuildStatusResponse.

        Parameters echoed back to user for debugging.  # noqa: E501

        :param parameters: The parameters of this InspectionBuildStatusResponse.  # noqa: E501
        :type: object
        """
        if parameters is None:
            raise ValueError("Invalid value for `parameters`, must not be `None`")  # noqa: E501

        self._parameters = parameters

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(InspectionBuildStatusResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InspectionBuildStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
