# Repository Structure

## Directories

The repository is organized into several directories, each serving a specific purpose. Directories containing refined data contracts are identified by `businessDomainName` and are located within the `data_contracts` directory.

### Directory Overview

| Directory         | Purpose                                                                      |
|-------------------|------------------------------------------------------------------------------|
| `/data_contracts` | Contains the Data Contract YAML files.                                       |
| `/.schema`        | Holds the Data Contract schema definition files.                             |
| `/.scripts`       | Contains scripts for automating various aspects of data contract management. |
| `/.templates`     | Includes template files for use with the `VSCode Template` extension.        |
| `/.vscode`        | Configuration files to enhance usability within VSCode.                      |
| `/docs`           | Documentation related to the repository.                                     |

## Data Contract Files

Data contract files must adhere to the following guidelines:

- **Format**: Files should be authored in YAML format.
- **Schema Compliance**: They must follow the schema definition provided in the repository. The YAML extension for VSCode offers helpful features for this.
- **Directory Placement**: Save files in the directory corresponding to the `businessDomainName` within the `/data_contracts` directory. Domain directories are named according to the 'Business Domain', with underscores replacing spaces.
- **File Naming**: Use a `.yaml` file extension. Name the file according to the `collectionName`, which is a logical grouping defined as follows:

  - **Collection Name Definition**: 
    - A distinct name identifying a grouping of related datasets. This allows for the segregation of datasets into smaller collections within a single domain. For instance, in the security domain, managing all products under one collection could be cumbersome. A specific example is 'Web Proxy', which consists of several datasets. Creating a unique collection for it simplifies organization and management.

By adhering to these guidelines, you ensure consistency and maintainability within the repository.