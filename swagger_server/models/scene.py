# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.action_mapping import ActionMapping  # noqa: F401,E501
from swagger_server.models.action_type_enum import ActionTypeEnum  # noqa: F401,E501
from swagger_server.models.conditions import Conditions  # noqa: F401,E501
from swagger_server.models.probe_config import ProbeConfig  # noqa: F401,E501
from swagger_server.models.semantic_type_enum import SemanticTypeEnum  # noqa: F401,E501
from swagger_server.models.state import State  # noqa: F401,E501
from swagger_server.models.tagging import Tagging  # noqa: F401,E501
from swagger_server import util


class Scene(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, state: State=None, next_scene: str=None, end_scene_allowed: bool=None, persist_characters: bool=None, removed_characters: List=None, probe_config: List[ProbeConfig]=None, tagging: Tagging=None, action_mapping: List[ActionMapping]=None, restricted_actions: List[ActionTypeEnum]=None, transition_semantics: SemanticTypeEnum=None, transitions: Conditions=None):  # noqa: E501
        """Scene - a model defined in Swagger

        :param id: The id of this Scene.  # noqa: E501
        :type id: str
        :param state: The state of this Scene.  # noqa: E501
        :type state: State
        :param next_scene: The next_scene of this Scene.  # noqa: E501
        :type next_scene: str
        :param end_scene_allowed: The end_scene_allowed of this Scene.  # noqa: E501
        :type end_scene_allowed: bool
        :param persist_characters: The persist_characters of this Scene.  # noqa: E501
        :type persist_characters: bool
        :param removed_characters: The removed_characters of this Scene.  # noqa: E501
        :type removed_characters: List
        :param probe_config: The probe_config of this Scene.  # noqa: E501
        :type probe_config: List[ProbeConfig]
        :param tagging: The tagging of this Scene.  # noqa: E501
        :type tagging: Tagging
        :param action_mapping: The action_mapping of this Scene.  # noqa: E501
        :type action_mapping: List[ActionMapping]
        :param restricted_actions: The restricted_actions of this Scene.  # noqa: E501
        :type restricted_actions: List[ActionTypeEnum]
        :param transition_semantics: The transition_semantics of this Scene.  # noqa: E501
        :type transition_semantics: SemanticTypeEnum
        :param transitions: The transitions of this Scene.  # noqa: E501
        :type transitions: Conditions
        """
        self.swagger_types = {
            'id': str,
            'state': State,
            'next_scene': str,
            'end_scene_allowed': bool,
            'persist_characters': bool,
            'removed_characters': List,
            'probe_config': List[ProbeConfig],
            'tagging': Tagging,
            'action_mapping': List[ActionMapping],
            'restricted_actions': List[ActionTypeEnum],
            'transition_semantics': SemanticTypeEnum,
            'transitions': Conditions
        }

        self.attribute_map = {
            'id': 'id',
            'state': 'state',
            'next_scene': 'next_scene',
            'end_scene_allowed': 'end_scene_allowed',
            'persist_characters': 'persist_characters',
            'removed_characters': 'removed_characters',
            'probe_config': 'probe_config',
            'tagging': 'tagging',
            'action_mapping': 'action_mapping',
            'restricted_actions': 'restricted_actions',
            'transition_semantics': 'transition_semantics',
            'transitions': 'transitions'
        }
        self._id = id
        self._state = state
        self._next_scene = next_scene
        self._end_scene_allowed = end_scene_allowed
        self._persist_characters = persist_characters
        self._removed_characters = removed_characters
        self._probe_config = probe_config
        self._tagging = tagging
        self._action_mapping = action_mapping
        self._restricted_actions = restricted_actions
        self._transition_semantics = transition_semantics
        self._transitions = transitions

    @classmethod
    def from_dict(cls, dikt) -> 'Scene':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Scene of this Scene.  # noqa: E501
        :rtype: Scene
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Scene.

        The scene ID, unique throughout the scenario  # noqa: E501

        :return: The id of this Scene.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Scene.

        The scene ID, unique throughout the scenario  # noqa: E501

        :param id: The id of this Scene.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def state(self) -> State:
        """Gets the state of this Scene.


        :return: The state of this Scene.
        :rtype: State
        """
        return self._state

    @state.setter
    def state(self, state: State):
        """Sets the state of this Scene.


        :param state: The state of this Scene.
        :type state: State
        """

        self._state = state

    @property
    def next_scene(self) -> str:
        """Gets the next_scene of this Scene.

        The ID of the default next scene in the scenario; if empty or missing, then by default this is the last scene.  # noqa: E501

        :return: The next_scene of this Scene.
        :rtype: str
        """
        return self._next_scene

    @next_scene.setter
    def next_scene(self, next_scene: str):
        """Sets the next_scene of this Scene.

        The ID of the default next scene in the scenario; if empty or missing, then by default this is the last scene.  # noqa: E501

        :param next_scene: The next_scene of this Scene.
        :type next_scene: str
        """

        self._next_scene = next_scene

    @property
    def end_scene_allowed(self) -> bool:
        """Gets the end_scene_allowed of this Scene.

        Whether ADMs can explicitly end the scene  # noqa: E501

        :return: The end_scene_allowed of this Scene.
        :rtype: bool
        """
        return self._end_scene_allowed

    @end_scene_allowed.setter
    def end_scene_allowed(self, end_scene_allowed: bool):
        """Sets the end_scene_allowed of this Scene.

        Whether ADMs can explicitly end the scene  # noqa: E501

        :param end_scene_allowed: The end_scene_allowed of this Scene.
        :type end_scene_allowed: bool
        """
        if end_scene_allowed is None:
            raise ValueError("Invalid value for `end_scene_allowed`, must not be `None`")  # noqa: E501

        self._end_scene_allowed = end_scene_allowed

    @property
    def persist_characters(self) -> bool:
        """Gets the persist_characters of this Scene.

        Whether characters should persist from the previous scene  # noqa: E501

        :return: The persist_characters of this Scene.
        :rtype: bool
        """
        return self._persist_characters

    @persist_characters.setter
    def persist_characters(self, persist_characters: bool):
        """Sets the persist_characters of this Scene.

        Whether characters should persist from the previous scene  # noqa: E501

        :param persist_characters: The persist_characters of this Scene.
        :type persist_characters: bool
        """

        self._persist_characters = persist_characters

    @property
    def removed_characters(self) -> List:
        """Gets the removed_characters of this Scene.


        :return: The removed_characters of this Scene.
        :rtype: List
        """
        return self._removed_characters

    @removed_characters.setter
    def removed_characters(self, removed_characters: List):
        """Sets the removed_characters of this Scene.


        :param removed_characters: The removed_characters of this Scene.
        :type removed_characters: List
        """

        self._removed_characters = removed_characters

    @property
    def probe_config(self) -> List[ProbeConfig]:
        """Gets the probe_config of this Scene.

        TA1-provided probe configuration, ignored by TA3  # noqa: E501

        :return: The probe_config of this Scene.
        :rtype: List[ProbeConfig]
        """
        return self._probe_config

    @probe_config.setter
    def probe_config(self, probe_config: List[ProbeConfig]):
        """Sets the probe_config of this Scene.

        TA1-provided probe configuration, ignored by TA3  # noqa: E501

        :param probe_config: The probe_config of this Scene.
        :type probe_config: List[ProbeConfig]
        """

        self._probe_config = probe_config

    @property
    def tagging(self) -> Tagging:
        """Gets the tagging of this Scene.


        :return: The tagging of this Scene.
        :rtype: Tagging
        """
        return self._tagging

    @tagging.setter
    def tagging(self, tagging: Tagging):
        """Sets the tagging of this Scene.


        :param tagging: The tagging of this Scene.
        :type tagging: Tagging
        """

        self._tagging = tagging

    @property
    def action_mapping(self) -> List[ActionMapping]:
        """Gets the action_mapping of this Scene.

        List of actions with details of how those actions map to probe responses  # noqa: E501

        :return: The action_mapping of this Scene.
        :rtype: List[ActionMapping]
        """
        return self._action_mapping

    @action_mapping.setter
    def action_mapping(self, action_mapping: List[ActionMapping]):
        """Sets the action_mapping of this Scene.

        List of actions with details of how those actions map to probe responses  # noqa: E501

        :param action_mapping: The action_mapping of this Scene.
        :type action_mapping: List[ActionMapping]
        """
        if action_mapping is None:
            raise ValueError("Invalid value for `action_mapping`, must not be `None`")  # noqa: E501

        self._action_mapping = action_mapping

    @property
    def restricted_actions(self) -> List[ActionTypeEnum]:
        """Gets the restricted_actions of this Scene.

        List of actions that will be excluded from get_available_actions  # noqa: E501

        :return: The restricted_actions of this Scene.
        :rtype: List[ActionTypeEnum]
        """
        return self._restricted_actions

    @restricted_actions.setter
    def restricted_actions(self, restricted_actions: List[ActionTypeEnum]):
        """Sets the restricted_actions of this Scene.

        List of actions that will be excluded from get_available_actions  # noqa: E501

        :param restricted_actions: The restricted_actions of this Scene.
        :type restricted_actions: List[ActionTypeEnum]
        """

        self._restricted_actions = restricted_actions

    @property
    def transition_semantics(self) -> SemanticTypeEnum:
        """Gets the transition_semantics of this Scene.


        :return: The transition_semantics of this Scene.
        :rtype: SemanticTypeEnum
        """
        return self._transition_semantics

    @transition_semantics.setter
    def transition_semantics(self, transition_semantics: SemanticTypeEnum):
        """Sets the transition_semantics of this Scene.


        :param transition_semantics: The transition_semantics of this Scene.
        :type transition_semantics: SemanticTypeEnum
        """

        self._transition_semantics = transition_semantics

    @property
    def transitions(self) -> Conditions:
        """Gets the transitions of this Scene.


        :return: The transitions of this Scene.
        :rtype: Conditions
        """
        return self._transitions

    @transitions.setter
    def transitions(self, transitions: Conditions):
        """Sets the transitions of this Scene.


        :param transitions: The transitions of this Scene.
        :type transitions: Conditions
        """

        self._transitions = transitions
