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

from cinder.tests.functional import api_samples_test_base as test_base


class LimitsSampleJsonTest(test_base.VolumesSampleBase):
    sample_dir = "limits"

    def setUp(self):
        super(LimitsSampleJsonTest, self).setUp()

    def test_limits_get(self):
        response = self._do_get('limits')
        self._verify_response('limits-show-response', {}, response, 200)
