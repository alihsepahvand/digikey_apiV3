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


class CategoriesResponse(object):
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
        'product_count': 'int',
        'categories': 'list[Category]'
    }

    attribute_map = {
        'product_count': 'ProductCount',
        'categories': 'Categories'
    }

    def __init__(self, product_count=None, categories=None, _configuration=None):  # noqa: E501
        """CategoriesResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._product_count = None
        self._categories = None
        self.discriminator = None

        if product_count is not None:
            self.product_count = product_count
        if categories is not None:
            self.categories = categories

    @property
    def product_count(self):
        """Gets the product_count of this CategoriesResponse.  # noqa: E501

        Count of Products  # noqa: E501

        :return: The product_count of this CategoriesResponse.  # noqa: E501
        :rtype: int
        """
        return self._product_count

    @product_count.setter
    def product_count(self, product_count):
        """Sets the product_count of this CategoriesResponse.

        Count of Products  # noqa: E501

        :param product_count: The product_count of this CategoriesResponse.  # noqa: E501
        :type: int
        """

        self._product_count = product_count

    @property
    def categories(self):
        """Gets the categories of this CategoriesResponse.  # noqa: E501

        List of Categories  # noqa: E501

        :return: The categories of this CategoriesResponse.  # noqa: E501
        :rtype: list[Category]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this CategoriesResponse.

        List of Categories  # noqa: E501

        :param categories: The categories of this CategoriesResponse.  # noqa: E501
        :type: list[Category]
        """

        self._categories = categories

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
        if issubclass(CategoriesResponse, dict):
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
        if not isinstance(other, CategoriesResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CategoriesResponse):
            return True

        return self.to_dict() != other.to_dict()
