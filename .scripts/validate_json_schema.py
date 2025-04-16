# @license
# Copyright 2022 Progressive Casualty Insurance Company. All Rights Reserved.

# Use of this source code is governed by an MIT license that can be found in
# the LICENSE file at https://github.com/Progressive/log-data-contracts/blob/main/LICENSE.md

import json
from jsonschema import Draft7Validator

with open("schema/splunk_data_contract_schema.json",encoding='utf8') as schema:
    schema_text = json.load(schema)

try:
    Draft7Validator.check_schema(schema=schema_text)
    print("The JSON schema is valid")
except Exception as e:
    print("The JSON schema failed validation")
    print(e)