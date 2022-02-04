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
# Snippet for RestartMigrationJob
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-dms


# [START datamigration_generated_clouddms_v1_DataMigrationService_RestartMigrationJob_sync]
from google.cloud import clouddms_v1


def sample_restart_migration_job():
    # Create a client
    client = clouddms_v1.DataMigrationServiceClient()

    # Initialize request argument(s)
    request = clouddms_v1.RestartMigrationJobRequest(
    )

    # Make the request
    operation = client.restart_migration_job(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()
    print(response)

# [END datamigration_generated_clouddms_v1_DataMigrationService_RestartMigrationJob_sync]
