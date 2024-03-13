# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class SoundRestrictionEnum(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    UNRESTRICTED = "unrestricted"
    MINIMAL = "minimal"
    MODERATE = "moderate"
    SEVERE = "severe"
    EXTREME = "extreme"
    def __init__(self):  # noqa: E501
        """SoundRestrictionEnum - a model defined in Swagger

        """
        self.swagger_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'SoundRestrictionEnum':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SoundRestrictionEnum of this SoundRestrictionEnum.  # noqa: E501
        :rtype: SoundRestrictionEnum
        """
        return util.deserialize_model(dikt, cls)
