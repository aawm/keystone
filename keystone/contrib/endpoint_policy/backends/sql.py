# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import logging

from keystone.endpoint_policy.backends import sql
from keystone.openstack.common import versionutils

LOG = logging.getLogger(__name__)

_OLD = 'keystone.contrib.endpoint_policy.backends.sql.EndpointPolicy'
_NEW = 'keystone.endpoint_policy.backends.sql.EndpointPolicy'


class EndpointPolicy(sql.EndpointPolicy):

    @versionutils.deprecated(versionutils.deprecated.LIBERTY,
                             in_favor_of=_NEW,
                             remove_in=1,
                             what=_OLD)
    def __init__(self, *args, **kwargs):
        super(EndpointPolicy, self).__init__(*args, **kwargs)
