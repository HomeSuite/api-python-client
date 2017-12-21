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


class CheckCreationRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, type=None, redirect_uri=None, reports=None, report_type_groups=None, criminal_history_report_details=None, tags=None, suppress_form_emails=None, charge_applicant_for_check=None):
        """
        CheckCreationRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'type': 'str',
            'redirect_uri': 'str',
            'reports': 'list[Report]',
            'report_type_groups': 'list[str]',
            'criminal_history_report_details': 'object',
            'tags': 'list[str]',
            'suppress_form_emails': 'bool',
            'charge_applicant_for_check': 'bool'
        }

        self.attribute_map = {
            'type': 'type',
            'redirect_uri': 'redirect_uri',
            'reports': 'reports',
            'report_type_groups': 'report_type_groups',
            'criminal_history_report_details': 'criminal_history_report_details',
            'tags': 'tags',
            'suppress_form_emails': 'suppress_form_emails',
            'charge_applicant_for_check': 'charge_applicant_for_check'
        }

        self._type = type
        self._redirect_uri = redirect_uri
        self._reports = reports
        self._report_type_groups = report_type_groups
        self._criminal_history_report_details = criminal_history_report_details
        self._tags = tags
        self._suppress_form_emails = suppress_form_emails
        self._charge_applicant_for_check = charge_applicant_for_check


    @property
    def type(self):
        """
        Gets the type of this CheckCreationRequest.
        standard or express

        :return: The type of this CheckCreationRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CheckCreationRequest.
        standard or express

        :param type: The type of this CheckCreationRequest.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def redirect_uri(self):
        """
        Gets the redirect_uri of this CheckCreationRequest.
        For standard checks, redirect to this URI when the applicant has submitted their data.

        :return: The redirect_uri of this CheckCreationRequest.
        :rtype: str
        """
        return self._redirect_uri

    @redirect_uri.setter
    def redirect_uri(self, redirect_uri):
        """
        Sets the redirect_uri of this CheckCreationRequest.
        For standard checks, redirect to this URI when the applicant has submitted their data.

        :param redirect_uri: The redirect_uri of this CheckCreationRequest.
        :type: str
        """

        self._redirect_uri = redirect_uri

    @property
    def reports(self):
        """
        Gets the reports of this CheckCreationRequest.
        Array of Reports being requested for this check.

        :return: The reports of this CheckCreationRequest.
        :rtype: list[Report]
        """
        return self._reports

    @reports.setter
    def reports(self, reports):
        """
        Sets the reports of this CheckCreationRequest.
        Array of Reports being requested for this check.

        :param reports: The reports of this CheckCreationRequest.
        :type: list[Report]
        """

        self._reports = reports

    @property
    def report_type_groups(self):
        """
        Gets the report_type_groups of this CheckCreationRequest.
        Array containing ids of the Report type groups being requested for.

        :return: The report_type_groups of this CheckCreationRequest.
        :rtype: list[str]
        """
        return self._report_type_groups

    @report_type_groups.setter
    def report_type_groups(self, report_type_groups):
        """
        Sets the report_type_groups of this CheckCreationRequest.
        Array containing ids of the Report type groups being requested for.

        :param report_type_groups: The report_type_groups of this CheckCreationRequest.
        :type: list[str]
        """

        self._report_type_groups = report_type_groups

    @property
    def criminal_history_report_details(self):
        """
        Gets the criminal_history_report_details of this CheckCreationRequest.
        Hash containing properties required for standard or enhanced UK criminal history reports. Only required for checks containing these specific reports. See Criminal history report details arguments.

        :return: The criminal_history_report_details of this CheckCreationRequest.
        :rtype: object
        """
        return self._criminal_history_report_details

    @criminal_history_report_details.setter
    def criminal_history_report_details(self, criminal_history_report_details):
        """
        Sets the criminal_history_report_details of this CheckCreationRequest.
        Hash containing properties required for standard or enhanced UK criminal history reports. Only required for checks containing these specific reports. See Criminal history report details arguments.

        :param criminal_history_report_details: The criminal_history_report_details of this CheckCreationRequest.
        :type: object
        """

        self._criminal_history_report_details = criminal_history_report_details

    @property
    def tags(self):
        """
        Gets the tags of this CheckCreationRequest.
        Array of tags being assigned to this check.

        :return: The tags of this CheckCreationRequest.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this CheckCreationRequest.
        Array of tags being assigned to this check.

        :param tags: The tags of this CheckCreationRequest.
        :type: list[str]
        """

        self._tags = tags

    @property
    def suppress_form_emails(self):
        """
        Gets the suppress_form_emails of this CheckCreationRequest.
        For standard checks, applicant form will not be automatically sent if this is set to true. You can manually send the form at any time after the check has been created, using the link found in the form_uri attribute of the check object. Defaults to false (i.e., form will be sent automatically by default).

        :return: The suppress_form_emails of this CheckCreationRequest.
        :rtype: bool
        """
        return self._suppress_form_emails

    @suppress_form_emails.setter
    def suppress_form_emails(self, suppress_form_emails):
        """
        Sets the suppress_form_emails of this CheckCreationRequest.
        For standard checks, applicant form will not be automatically sent if this is set to true. You can manually send the form at any time after the check has been created, using the link found in the form_uri attribute of the check object. Defaults to false (i.e., form will be sent automatically by default).

        :param suppress_form_emails: The suppress_form_emails of this CheckCreationRequest.
        :type: bool
        """

        self._suppress_form_emails = suppress_form_emails

    @property
    def charge_applicant_for_check(self):
        """
        Gets the charge_applicant_for_check of this CheckCreationRequest.
        For standard checks, applicants will be presented with a mandatory payment screen before they can submit the applicant form, if this is set to true. In this case, your account will not be charged. Defaults to false.

        :return: The charge_applicant_for_check of this CheckCreationRequest.
        :rtype: bool
        """
        return self._charge_applicant_for_check

    @charge_applicant_for_check.setter
    def charge_applicant_for_check(self, charge_applicant_for_check):
        """
        Sets the charge_applicant_for_check of this CheckCreationRequest.
        For standard checks, applicants will be presented with a mandatory payment screen before they can submit the applicant form, if this is set to true. In this case, your account will not be charged. Defaults to false.

        :param charge_applicant_for_check: The charge_applicant_for_check of this CheckCreationRequest.
        :type: bool
        """

        self._charge_applicant_for_check = charge_applicant_for_check

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
