# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ResourceCostProperties(Model):
    """The properties of a resource cost item.

    :param resourcename: The name of the resource.
    :type resourcename: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param resource_cost: The cost component of the resource cost item.
    :type resource_cost: float
    :param owner: The email address of the owner of the resource
    :type owner: str
    :param category: The category of the resource. For VM this will be set to
     its size, for storage account it will be set to standard or premium
    :type category: str
    :param exists: Whether the resource still exists or not
    :type exists: bool
    :param resource_type: The logical resource type (ex. virtualmachine,
     storageaccount)
    :type resource_type: str
    """ 

    _attribute_map = {
        'resourcename': {'key': 'resourcename', 'type': 'str'},
        'resource_group_name': {'key': 'resourceGroupName', 'type': 'str'},
        'resource_cost': {'key': 'resourceCost', 'type': 'float'},
        'owner': {'key': 'owner', 'type': 'str'},
        'category': {'key': 'category', 'type': 'str'},
        'exists': {'key': 'exists', 'type': 'bool'},
        'resource_type': {'key': 'resourceType', 'type': 'str'},
    }

    def __init__(self, resourcename=None, resource_group_name=None, resource_cost=None, owner=None, category=None, exists=None, resource_type=None):
        self.resourcename = resourcename
        self.resource_group_name = resource_group_name
        self.resource_cost = resource_cost
        self.owner = owner
        self.category = category
        self.exists = exists
        self.resource_type = resource_type
