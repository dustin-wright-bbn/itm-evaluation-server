# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.tag_label import TagLabel  # noqa: F401,E501
from swagger_server import util


class TriageCategory(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, tag_label: TagLabel=None, description: str=None, criteria: str=None):  # noqa: E501
        """TriageCategory - a model defined in Swagger

        :param tag_label: The tag_label of this TriageCategory.  # noqa: E501
        :type tag_label: TagLabel
        :param description: The description of this TriageCategory.  # noqa: E501
        :type description: str
        :param criteria: The criteria of this TriageCategory.  # noqa: E501
        :type criteria: str
        """
        self.swagger_types = {
            'tag_label': TagLabel,
            'description': str,
            'criteria': str
        }

        self.attribute_map = {
            'tag_label': 'tagLabel',
            'description': 'description',
            'criteria': 'criteria'
        }
        self._tag_label = tag_label
        self._description = description
        self._criteria = criteria

    @classmethod
    def from_dict(cls, dikt) -> 'TriageCategory':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TriageCategory of this TriageCategory.  # noqa: E501
        :rtype: TriageCategory
        """
        return util.deserialize_model(dikt, cls)

    @property
    def tag_label(self) -> TagLabel:
        """Gets the tag_label of this TriageCategory.


        :return: The tag_label of this TriageCategory.
        :rtype: TagLabel
        """
        return self._tag_label

    @tag_label.setter
    def tag_label(self, tag_label: TagLabel):
        """Sets the tag_label of this TriageCategory.


        :param tag_label: The tag_label of this TriageCategory.
        :type tag_label: TagLabel
        """

        self._tag_label = tag_label

    @property
    def description(self) -> str:
        """Gets the description of this TriageCategory.

        a one-line description of the tagLabel category  # noqa: E501

        :return: The description of this TriageCategory.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this TriageCategory.

        a one-line description of the tagLabel category  # noqa: E501

        :param description: The description of this TriageCategory.
        :type description: str
        """

        self._description = description

    @property
    def criteria(self) -> str:
        """Gets the criteria of this TriageCategory.

        detailed criteria for the tagLabel category  # noqa: E501

        :return: The criteria of this TriageCategory.
        :rtype: str
        """
        return self._criteria

    @criteria.setter
    def criteria(self, criteria: str):
        """Sets the criteria of this TriageCategory.

        detailed criteria for the tagLabel category  # noqa: E501

        :param criteria: The criteria of this TriageCategory.
        :type criteria: str
        """

        self._criteria = criteria
