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


class LimitedTaxonomy(object):
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
        'children': 'list[LimitedTaxonomy]',
        'product_count': 'int',
        'new_product_count': 'int',
        'parameter_id': 'int',
        'value_id': 'str',
        'parameter': 'str',
        'value': 'str'
    }

    attribute_map = {
        'children': 'Children',
        'product_count': 'ProductCount',
        'new_product_count': 'NewProductCount',
        'parameter_id': 'ParameterId',
        'value_id': 'ValueId',
        'parameter': 'Parameter',
        'value': 'Value'
    }

    def __init__(self, children=None, product_count=None, new_product_count=None, parameter_id=None, value_id=None, parameter=None, value=None, _configuration=None):  # noqa: E501
        """LimitedTaxonomy - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._children = None
        self._product_count = None
        self._new_product_count = None
        self._parameter_id = None
        self._value_id = None
        self._parameter = None
        self._value = None
        self.discriminator = None

        if children is not None:
            self.children = children
        if product_count is not None:
            self.product_count = product_count
        if new_product_count is not None:
            self.new_product_count = new_product_count
        if parameter_id is not None:
            self.parameter_id = parameter_id
        if value_id is not None:
            self.value_id = value_id
        if parameter is not None:
            self.parameter = parameter
        if value is not None:
            self.value = value

    @property
    def children(self):
        """Gets the children of this LimitedTaxonomy.  # noqa: E501

        List of taxonomies contained within this taxonomy.  # noqa: E501

        :return: The children of this LimitedTaxonomy.  # noqa: E501
        :rtype: list[LimitedTaxonomy]
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this LimitedTaxonomy.

        List of taxonomies contained within this taxonomy.  # noqa: E501

        :param children: The children of this LimitedTaxonomy.  # noqa: E501
        :type: list[LimitedTaxonomy]
        """

        self._children = children

    @property
    def product_count(self):
        """Gets the product_count of this LimitedTaxonomy.  # noqa: E501

        The number of products contained within this taxonomy.  # noqa: E501

        :return: The product_count of this LimitedTaxonomy.  # noqa: E501
        :rtype: int
        """
        return self._product_count

    @product_count.setter
    def product_count(self, product_count):
        """Sets the product_count of this LimitedTaxonomy.

        The number of products contained within this taxonomy.  # noqa: E501

        :param product_count: The product_count of this LimitedTaxonomy.  # noqa: E501
        :type: int
        """

        self._product_count = product_count

    @property
    def new_product_count(self):
        """Gets the new_product_count of this LimitedTaxonomy.  # noqa: E501

        The number of new products contained within this taxonomy.  # noqa: E501

        :return: The new_product_count of this LimitedTaxonomy.  # noqa: E501
        :rtype: int
        """
        return self._new_product_count

    @new_product_count.setter
    def new_product_count(self, new_product_count):
        """Sets the new_product_count of this LimitedTaxonomy.

        The number of new products contained within this taxonomy.  # noqa: E501

        :param new_product_count: The new_product_count of this LimitedTaxonomy.  # noqa: E501
        :type: int
        """

        self._new_product_count = new_product_count

    @property
    def parameter_id(self):
        """Gets the parameter_id of this LimitedTaxonomy.  # noqa: E501

        The Id of the parameter.  # noqa: E501

        :return: The parameter_id of this LimitedTaxonomy.  # noqa: E501
        :rtype: int
        """
        return self._parameter_id

    @parameter_id.setter
    def parameter_id(self, parameter_id):
        """Sets the parameter_id of this LimitedTaxonomy.

        The Id of the parameter.  # noqa: E501

        :param parameter_id: The parameter_id of this LimitedTaxonomy.  # noqa: E501
        :type: int
        """

        self._parameter_id = parameter_id

    @property
    def value_id(self):
        """Gets the value_id of this LimitedTaxonomy.  # noqa: E501

        The Id of the value.  # noqa: E501

        :return: The value_id of this LimitedTaxonomy.  # noqa: E501
        :rtype: str
        """
        return self._value_id

    @value_id.setter
    def value_id(self, value_id):
        """Sets the value_id of this LimitedTaxonomy.

        The Id of the value.  # noqa: E501

        :param value_id: The value_id of this LimitedTaxonomy.  # noqa: E501
        :type: str
        """

        self._value_id = value_id

    @property
    def parameter(self):
        """Gets the parameter of this LimitedTaxonomy.  # noqa: E501

        The name of the parameter.  # noqa: E501

        :return: The parameter of this LimitedTaxonomy.  # noqa: E501
        :rtype: str
        """
        return self._parameter

    @parameter.setter
    def parameter(self, parameter):
        """Sets the parameter of this LimitedTaxonomy.

        The name of the parameter.  # noqa: E501

        :param parameter: The parameter of this LimitedTaxonomy.  # noqa: E501
        :type: str
        """

        self._parameter = parameter

    @property
    def value(self):
        """Gets the value of this LimitedTaxonomy.  # noqa: E501

        The name of the value.  # noqa: E501

        :return: The value of this LimitedTaxonomy.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this LimitedTaxonomy.

        The name of the value.  # noqa: E501

        :param value: The value of this LimitedTaxonomy.  # noqa: E501
        :type: str
        """

        self._value = value

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
        if issubclass(LimitedTaxonomy, dict):
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
        if not isinstance(other, LimitedTaxonomy):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LimitedTaxonomy):
            return True

        return self.to_dict() != other.to_dict()
