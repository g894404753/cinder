# Copyright (c) 2017 Huawei Technologies Co., Ltd.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from oslo_policy import policy

from cinder.policies import base

CREATE_POLICY = 'group:create'
UPDATE_POLICY = 'group:update'
GET_POLICY = 'group:get'
GET_ALL_POLICY = 'group:get_all'
GROUP_ATTRIBUTES_POLICY = 'group:group_project_attribute'

deprecated_get_all_groups = base.CinderDeprecatedRule(
    name=GET_ALL_POLICY,
    check_str=base.RULE_ADMIN_OR_OWNER
)
deprecated_create_group = base.CinderDeprecatedRule(
    name=CREATE_POLICY,
    check_str=""
)
deprecated_get_group = base.CinderDeprecatedRule(
    name=GET_POLICY,
    check_str=base.RULE_ADMIN_OR_OWNER
)
deprecated_update_group = base.CinderDeprecatedRule(
    name=UPDATE_POLICY,
    check_str=base.RULE_ADMIN_OR_OWNER,
)


groups_policies = [
    policy.DocumentedRuleDefault(
        name=GET_ALL_POLICY,
        check_str=base.SYSTEM_READER_OR_PROJECT_READER,
        description="List groups.",
        operations=[
            {
                'method': 'GET',
                'path': '/groups'
            },
            {
                'method': 'GET',
                'path': '/groups/detail'
            }
        ],
        deprecated_rule=deprecated_get_all_groups,
    ),
    policy.DocumentedRuleDefault(
        name=CREATE_POLICY,
        check_str=base.SYSTEM_ADMIN_OR_PROJECT_MEMBER,
        description="Create group.",
        operations=[
            {
                'method': 'POST',
                'path': '/groups'
            }
        ],
        deprecated_rule=deprecated_create_group,
    ),
    policy.DocumentedRuleDefault(
        name=GET_POLICY,
        check_str=base.SYSTEM_READER_OR_PROJECT_READER,
        description="Show group.",
        operations=[
            {
                'method': 'GET',
                'path': '/groups/{group_id}'
            }
        ],
        deprecated_rule=deprecated_get_group,
    ),
    policy.DocumentedRuleDefault(
        name=UPDATE_POLICY,
        check_str=base.SYSTEM_ADMIN_OR_PROJECT_MEMBER,
        description="Update group.",
        operations=[
            {
                'method': 'PUT',
                'path': '/groups/{group_id}'
            }
        ],
        deprecated_rule=deprecated_update_group,
    ),
    policy.DocumentedRuleDefault(
        name=GROUP_ATTRIBUTES_POLICY,
        check_str=base.RULE_ADMIN_API,
        description="List groups or show group with project attributes.",
        operations=[
            {
                'method': 'GET',
                'path': '/groups/{group_id}'
            },
            {
                'method': 'GET',
                'path': '/groups/detail'
            }
        ]
    ),
]


def list_rules():
    return groups_policies
