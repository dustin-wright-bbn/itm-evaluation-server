# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.aid_type_enum import AidTypeEnum  # noqa: F401,E501
from swagger_server.models.military_disposition_enum import MilitaryDispositionEnum  # noqa: F401,E501
from swagger_server import util


class Aid(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, delay: float=None, type: AidTypeEnum=None, role: int=None, patients_treated: List[MilitaryDispositionEnum]=None, max_transport: int=None):  # noqa: E501
        """Aid - a model defined in Swagger

        :param id: The id of this Aid.  # noqa: E501
        :type id: str
        :param delay: The delay of this Aid.  # noqa: E501
        :type delay: float
        :param type: The type of this Aid.  # noqa: E501
        :type type: AidTypeEnum
        :param role: The role of this Aid.  # noqa: E501
        :type role: int
        :param patients_treated: The patients_treated of this Aid.  # noqa: E501
        :type patients_treated: List[MilitaryDispositionEnum]
        :param max_transport: The max_transport of this Aid.  # noqa: E501
        :type max_transport: int
        """
        self.swagger_types = {
            'id': str,
            'delay': float,
            'type': AidTypeEnum,
            'role': int,
            'patients_treated': List[MilitaryDispositionEnum],
            'max_transport': int
        }

        self.attribute_map = {
            'id': 'id',
            'delay': 'delay',
            'type': 'type',
            'role': 'role',
            'patients_treated': 'patients_treated',
            'max_transport': 'max_transport'
        }
        self._id = id
        self._delay = delay
        self._type = type
        self._role = role
        self._patients_treated = patients_treated
        self._max_transport = max_transport

    @classmethod
    def from_dict(cls, dikt) -> 'Aid':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Aid of this Aid.  # noqa: E501
        :rtype: Aid
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Aid.

        An identifier for the aid opportunity, unique within the scene  # noqa: E501

        :return: The id of this Aid.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Aid.

        An identifier for the aid opportunity, unique within the scene  # noqa: E501

        :param id: The id of this Aid.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def delay(self) -> float:
        """Gets the delay of this Aid.

        Time until aid is available, in minutes; 0 means ready now  # noqa: E501

        :return: The delay of this Aid.
        :rtype: float
        """
        return self._delay

    @delay.setter
    def delay(self, delay: float):
        """Sets the delay of this Aid.

        Time until aid is available, in minutes; 0 means ready now  # noqa: E501

        :param delay: The delay of this Aid.
        :type delay: float
        """
        if delay is None:
            raise ValueError("Invalid value for `delay`, must not be `None`")  # noqa: E501

        self._delay = delay

    @property
    def type(self) -> AidTypeEnum:
        """Gets the type of this Aid.


        :return: The type of this Aid.
        :rtype: AidTypeEnum
        """
        return self._type

    @type.setter
    def type(self, type: AidTypeEnum):
        """Sets the type of this Aid.


        :param type: The type of this Aid.
        :type type: AidTypeEnum
        """

        self._type = type

    @property
    def role(self) -> int:
        """Gets the role of this Aid.

        The characterization of health support for the distribution of medical resources and capabilities; Role 1 has higher capability than Role 4. See [health.mil](https://health.mil/Reference-Center/Glossary-Terms/2018/06/22/Roles-of-Medical-Care)   # noqa: E501

        :return: The role of this Aid.
        :rtype: int
        """
        return self._role

    @role.setter
    def role(self, role: int):
        """Sets the role of this Aid.

        The characterization of health support for the distribution of medical resources and capabilities; Role 1 has higher capability than Role 4. See [health.mil](https://health.mil/Reference-Center/Glossary-Terms/2018/06/22/Roles-of-Medical-Care)   # noqa: E501

        :param role: The role of this Aid.
        :type role: int
        """

        self._role = role

    @property
    def patients_treated(self) -> List[MilitaryDispositionEnum]:
        """Gets the patients_treated of this Aid.

        A list of types of patients that can be helped; if omitted, then no restrictions or restrictions are irrelevant  # noqa: E501

        :return: The patients_treated of this Aid.
        :rtype: List[MilitaryDispositionEnum]
        """
        return self._patients_treated

    @patients_treated.setter
    def patients_treated(self, patients_treated: List[MilitaryDispositionEnum]):
        """Sets the patients_treated of this Aid.

        A list of types of patients that can be helped; if omitted, then no restrictions or restrictions are irrelevant  # noqa: E501

        :param patients_treated: The patients_treated of this Aid.
        :type patients_treated: List[MilitaryDispositionEnum]
        """

        self._patients_treated = patients_treated

    @property
    def max_transport(self) -> int:
        """Gets the max_transport of this Aid.

        Maximum number of casualties that can be accommodated  # noqa: E501

        :return: The max_transport of this Aid.
        :rtype: int
        """
        return self._max_transport

    @max_transport.setter
    def max_transport(self, max_transport: int):
        """Sets the max_transport of this Aid.

        Maximum number of casualties that can be accommodated  # noqa: E501

        :param max_transport: The max_transport of this Aid.
        :type max_transport: int
        """

        self._max_transport = max_transport