# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class MilitaryRankEnum(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    E_1 = "E-1"
    E_2 = "E-2"
    E_3 = "E-3"
    E_4 = "E-4"
    E_5 = "E-5"
    E_6 = "E-6"
    E_7 = "E-7"
    E_8 = "E-8"
    E_9 = "E-9"
    E_9_SPECIAL_ = "E-9 (special)"
    W_1 = "W-1"
    W_2 = "W-2"
    W_3 = "W-3"
    W_4 = "W-4"
    W_5 = "W-5"
    O_1 = "O-1"
    O_2 = "O-2"
    O_3 = "O-3"
    O_4 = "O-4"
    O_5 = "O-5"
    O_6 = "O-6"
    O_7 = "O-7"
    O_8 = "O-8"
    O_9 = "O-9"
    O_10 = "O-10"
    SPECIAL = "Special"
    SPECIAL_NAVY_ = "Special (Navy)"
    SPECIAL_COAST_GUARD_ = "Special (Coast Guard)"
    def __init__(self):  # noqa: E501
        """MilitaryRankEnum - a model defined in Swagger

        """
        self.swagger_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'MilitaryRankEnum':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MilitaryRankEnum of this MilitaryRankEnum.  # noqa: E501
        :rtype: MilitaryRankEnum
        """
        return util.deserialize_model(dikt, cls)
