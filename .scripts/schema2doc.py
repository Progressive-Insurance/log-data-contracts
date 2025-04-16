# @license
# Copyright 2022 Progressive Casualty Insurance Company. All Rights Reserved.

# Use of this source code is governed by an MIT license that can be found in
# the LICENSE file at https://github.com/Progressive/log-data-contracts/blob/main/LICENSE.md

import json
import jsonschema2md

parser = jsonschema2md.Parser(
    examples_as_yaml=True,
    show_examples="all"
)

with open("schema/splunk_data_contract_schema.json", "r") as json_file:
    mdMonitoringDataContractSchema = parser.parse_schema(json.load(json_file))

with open("docs/schema.md", "w") as monDataContractSchemaDocFile:
    monDataContractSchemaDocFile.write(''.join(mdMonitoringDataContractSchema))
    monDataContractSchemaDocFile.write("\n")

