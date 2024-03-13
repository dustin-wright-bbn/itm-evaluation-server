# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class RaceEnum(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    AMERICAN_INDIAN = "American Indian"
    WHITE = "White"
    HISPANIC = "Hispanic"
    BLACK = "Black"
    ASIAN = "Asian"
    PACIFIC_ISLANDER = "Pacific Islander"
    def __init__(self):  # noqa: E501
        """RaceEnum - a model defined in Swagger

        """
        self.swagger_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'RaceEnum':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RaceEnum of this RaceEnum.  # noqa: E501
        :rtype: RaceEnum
        """
        return util.deserialize_model(dikt, cls)
