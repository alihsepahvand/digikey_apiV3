# coding: utf-8

"""
    PartSearch Api

    Search for products and retrieve details and pricing.  # noqa: E501

    OpenAPI spec version: Ps2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class ManufacturersResponse(object):
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
        'manufacturers': 'list[ManufacturerInfo]'
    }

    attribute_map = {
        'manufacturers': 'Manufacturers'
    }

    def __init__(self, manufacturers=None, _configuration=None):  # noqa: E501
        """ManufacturersResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._manufacturers = None
        self.discriminator = None

        if manufacturers is not None:
            self.manufacturers = manufacturers

    @property
    def manufacturers(self):
        """Gets the manufacturers of this ManufacturersResponse.  # noqa: E501

        List of Manufacturer Information  # noqa: E501

        :return: The manufacturers of this ManufacturersResponse.  # noqa: E501
        :rtype: list[ManufacturerInfo]
        """
        return self._manufacturers

    @manufacturers.setter
    def manufacturers(self, manufacturers):
        """Sets the manufacturers of this ManufacturersResponse.

        List of Manufacturer Information  # noqa: E501

        :param manufacturers: The manufacturers of this ManufacturersResponse.  # noqa: E501
        :type: list[ManufacturerInfo]
        """

        self._manufacturers = manufacturers

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
        if issubclass(ManufacturersResponse, dict):
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
        if not isinstance(other, ManufacturersResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ManufacturersResponse):
            return True

        return self.to_dict() != other.to_dict()
