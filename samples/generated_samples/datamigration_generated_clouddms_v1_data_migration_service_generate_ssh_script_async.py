# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Generated code. DO NOT EDIT!
#
# Snippet for GenerateSshScript
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-dms


# [START datamigration_generated_clouddms_v1_DataMigrationService_GenerateSshScript_async]
from google.cloud import clouddms_v1


async def sample_generate_ssh_script():
    # Create a client
    client = clouddms_v1.DataMigrationServiceAsyncClient()

    # Initialize request argument(s)
    vm_creation_config = clouddms_v1.VmCreationConfig()
    vm_creation_config.vm_machine_type = "vm_machine_type_value"

    request = clouddms_v1.GenerateSshScriptRequest(
        vm_creation_config=vm_creation_config,
        vm="vm_value",
    )

    # Make the request
    response = await client.generate_ssh_script(request=request)

    # Handle response
    print(response)

# [END datamigration_generated_clouddms_v1_DataMigrationService_GenerateSshScript_async]
