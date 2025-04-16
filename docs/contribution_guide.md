# Data Contract Contribution Guide

## Getting Started with a New Data Contract

### Follow Standard Git Branching Methods

1. **Clone this Repository**: Begin by cloning the repository to your local machine.

### Open the Repository in VSCode (Recommended)

1. **Open in VSCode**: Launch the cloned repository in Visual Studio Code (VSCode).
   - You may receive extension recommendations. It is advisable to accept these for an optimal experience.
2. **Create a New Feature Branch**: Start a new branch for your feature development.

### Collect Information About the Dataset

- Gather necessary information from the data Subject Matter Expert (SME) or data Steward. Required data elements are outlined in the schema definition file.
- Authoring a data contract is easiest in VSCode with the YAML add-on, which provides context-sensitive help and auto-fill capabilities.

#### Getting Started in VSCode

- Determine the `businessDomainName` and `collectionName` for the data contract. Refer to the schema definition for descriptions of these fields.
- Familiarize yourself with required elements for a new data product. Supported types include:
  - **`splunkDataset`**: Events or metrics in a Splunk Core index
  - **`splunkLookup`**: (Future implementation)

### Determine the Business Domain or Collection

- **Note**: Data contract files are located in a "domain" directory within the `./data_contracts` directory.
- If the business domain already exists, it will have a directory in the repository.
  - If not, create a new directory named using Initial Caps with underscores for spaces (e.g., `Cloud_Services` for "cloud services").
- Collections are grouped into `.yaml` files within `businessDomainName` directories. Edit an existing file if applicable, or create a new one if necessary.

### (Optional) Use the Template for a New Collection

If creating a new collection, the `Template` extension in VSCode can help populate the file with common fields:

1. **Create a New File**: Right-click on the directory and select `Template: Create new (with rename)`.
2. **Select a Template**: Choose the most applicable template from the list:
   - **Index or sourcetype contains wineventlog**: Use `data_contract-wineventlog-RENAME_ME.yaml`
   - **All other cases**: Use `data_contract-general-RENAME_ME.yaml`
3. **Name the File**: Provide a name for the collection's `.yaml` file.
4. **Populate Fields**: The template will pre-populate common fields. Use the YAML extension's mouse-over functions to determine which fields to keep or remove.

### Fill Out the Data Contract Elements in VSCode

- The 'JSON Schema' definition offers assistance and validation for data contracts in VSCode.

#### Tips:

- Elements with issues are highlighted with a wavy red line. Hover over them for contextual help.
- Use VSCode's context-sensitive features to auto-fill elements by pressing `<ctrl>+<spacebar>` on Windows or `<cmd>+<spacebar>` on Mac.

### Save and Commit Your Changes

1. **Save**: Ensure your `.yaml` file is saved in the correct `/data_contracts/<domain>` directory.
2. **Stage Changes**: Add your changes via the 'Source Control' pane in VSCode.
3. **Commit**: Include a work item ID in the commit message (e.g., `#3452332 new data contract for...`) to link it to a backlog item.
4. **Push/Sync**: Push your changes to the remote repository.

### Submit a Pull Request

1. **Pull Request**: Submit a pull request via the WebUI.
   - The repository pipeline will run, verifying schema compliance. If issues arise, review the logs for details and make necessary corrections.
2. **Approval and Completion**: Once approved, changes are merged into the 'main' branch.
3. **Publish**: The data contract changes are published to the Splunk KVStore `em_data_contracts`. View contents with the query: `| inputlookup em_data_contracts`