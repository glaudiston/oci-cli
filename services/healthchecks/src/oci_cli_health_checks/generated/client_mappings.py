# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

import oci
from oci_cli.cli_clients import CLIENT_MAP
from oci_cli.cli_clients import MODULE_TO_TYPE_MAPPINGS
from oci.healthchecks import HealthChecksClient

MODULE_TO_TYPE_MAPPINGS["healthchecks"] = oci.healthchecks.models.healthchecks_type_mapping
CLIENT_MAP["health_checks"] = HealthChecksClient
