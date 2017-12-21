# coding: utf-8

"""
    Onfido API

    The Onfido API is used to submit check requests.

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class GenericAddress(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, flat_number=None, building_number=None, building_name=None, street=None, sub_street=None, town=None, postcode=None, country=None):
        """
        GenericAddress - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'flat_number': 'str',
            'building_number': 'str',
            'building_name': 'str',
            'street': 'str',
            'sub_street': 'str',
            'town': 'str',
            'postcode': 'str',
            'country': 'str'
        }

        self.attribute_map = {
            'flat_number': 'flat_number',
            'building_number': 'building_number',
            'building_name': 'building_name',
            'street': 'street',
            'sub_street': 'sub_street',
            'town': 'town',
            'postcode': 'postcode',
            'country': 'country'
        }

        self._flat_number = flat_number
        self._building_number = building_number
        self._building_name = building_name
        self._street = street
        self._sub_street = sub_street
        self._town = town
        self._postcode = postcode
        self._country = country


    @property
    def flat_number(self):
        """
        Gets the flat_number of this GenericAddress.
        The flat number of this address

        :return: The flat_number of this GenericAddress.
        :rtype: str
        """
        return self._flat_number

    @flat_number.setter
    def flat_number(self, flat_number):
        """
        Sets the flat_number of this GenericAddress.
        The flat number of this address

        :param flat_number: The flat_number of this GenericAddress.
        :type: str
        """

        self._flat_number = flat_number

    @property
    def building_number(self):
        """
        Gets the building_number of this GenericAddress.
        The building number of this address

        :return: The building_number of this GenericAddress.
        :rtype: str
        """
        return self._building_number

    @building_number.setter
    def building_number(self, building_number):
        """
        Sets the building_number of this GenericAddress.
        The building number of this address

        :param building_number: The building_number of this GenericAddress.
        :type: str
        """

        self._building_number = building_number

    @property
    def building_name(self):
        """
        Gets the building_name of this GenericAddress.
        The building name of this address

        :return: The building_name of this GenericAddress.
        :rtype: str
        """
        return self._building_name

    @building_name.setter
    def building_name(self, building_name):
        """
        Sets the building_name of this GenericAddress.
        The building name of this address

        :param building_name: The building_name of this GenericAddress.
        :type: str
        """

        self._building_name = building_name

    @property
    def street(self):
        """
        Gets the street of this GenericAddress.
        The street of the applicant’s address

        :return: The street of this GenericAddress.
        :rtype: str
        """
        return self._street

    @street.setter
    def street(self, street):
        """
        Sets the street of this GenericAddress.
        The street of the applicant’s address

        :param street: The street of this GenericAddress.
        :type: str
        """

        self._street = street

    @property
    def sub_street(self):
        """
        Gets the sub_street of this GenericAddress.
        The sub-street of the applicant’s address

        :return: The sub_street of this GenericAddress.
        :rtype: str
        """
        return self._sub_street

    @sub_street.setter
    def sub_street(self, sub_street):
        """
        Sets the sub_street of this GenericAddress.
        The sub-street of the applicant’s address

        :param sub_street: The sub_street of this GenericAddress.
        :type: str
        """

        self._sub_street = sub_street

    @property
    def town(self):
        """
        Gets the town of this GenericAddress.
        The town of the applicant’s address

        :return: The town of this GenericAddress.
        :rtype: str
        """
        return self._town

    @town.setter
    def town(self, town):
        """
        Sets the town of this GenericAddress.
        The town of the applicant’s address

        :param town: The town of this GenericAddress.
        :type: str
        """

        self._town = town

    @property
    def postcode(self):
        """
        Gets the postcode of this GenericAddress.
        The postcode or ZIP of the applicant’s address

        :return: The postcode of this GenericAddress.
        :rtype: str
        """
        return self._postcode

    @postcode.setter
    def postcode(self, postcode):
        """
        Sets the postcode of this GenericAddress.
        The postcode or ZIP of the applicant’s address

        :param postcode: The postcode of this GenericAddress.
        :type: str
        """

        self._postcode = postcode

    @property
    def country(self):
        """
        Gets the country of this GenericAddress.
        The 3 character ISO country code of this address. For example, GBR is the country code for the United Kingdom

        :return: The country of this GenericAddress.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this GenericAddress.
        The 3 character ISO country code of this address. For example, GBR is the country code for the United Kingdom

        :param country: The country of this GenericAddress.
        :type: str
        """

        self._country = country

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other