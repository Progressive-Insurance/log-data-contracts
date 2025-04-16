# Splunk Data Contract

*Data Contract definition for Splunk 'Classic' datasets*

## Properties

- **`businessDomainName`** *(['string'], required)*: The name of the IT Architectural Domain to which the data products within this data contract apply. Refer to *[#/$def/businessDomainNames](#%24def/businessDomainNames)*.
- **`collectionName`** *(['string'], required)*: A distinct name identifying a grouping of related data products.  Provides a way for segregating datasets into smaller collections within a single domain. A sample use case would be for the security domain. Security owns many different products, and having them all contained in one collection might be burdensome for maintenance.  For example, 'Jimmy's Proxy', by itself consists of several datasets...so breaking that out into a unique collection makes management of the several data contract files more convenient.
- **`datasets`** *(['array'], required)*: An array of objects that describe distinct data products. Default: `"splunkDataset"`.
  - **Items** *(['object'])*: Cannot contain additional properties.
    - **`splunkDataset`** *(['object'])*: A distinct Splunk dataset is defined as a collection of events or metrics that are defined and maintained in Splunk for a specific business purpose.  A Splunk dataset can consist of metric or event (log) data. Cannot contain additional properties.
      - **`quantumName`** *(['string'], required)*: A 'quantum' being defined as, 'the minimum amount of any physical entity involved in an interaction', the 'quantumName' of a dataset should be a brief distinct name for the Splunk dataset.  If possible, a combination of <index>:<sourcetype> or <index>:<source> if those are distinct to this dataset. The field name `quantumName` is an "hommage" to the data contract work efforts of PayPal.
      - **`dataContractId`** *(['string'], required)*: A unique GUID identifier for this data contract/dataset. Activate 'Insert GUID' from the VSCode Command Palette to populate this using the 'Insert GUID' extension.
      - **`datasetDescription`** *(['string'], required)*: A description of the dataset--which ends up also being a description of the Splunk sourcetype if it is distinct to this dataset.
      - **`datasetStatusCode`**: The status of the dataset. Must be one of: `["proposed", "active", "deprecated", "retired"]`.
      - **`purposeDescription`** *(['string'], required)*: A sound and justifiable business purpose that dictates why this dataset is needed in Splunk.  e.g. A description of the business value that this data is intended to deliver.
      - **`datasetTypeCode`**: The type of Splunk data to which this Splunk Dataset can be categorized--the type of Splunk index in which the data will reside. Must be one of: `["event", "metric"]`.
      - **`consumptionModeCode`**: The normalized expected use case for the dataset's presense in Splunk. Must be one of: `["operational", "security", "compliance", "contextual"]`.
      - **`dataProductInitialSmeName`** *(['string'], required)*: The name of the person from whom the data onboarding was initially requested, reviewed, or confirmed.  This individual is only considered to be SME on this dataset during the initial onboarding.  This is not intended to be kept current as personnel changes occur, but to provide historical context of the dataset.
      - **`dataProductEmailDistributionName`** *(['string'])*: [Optional but strongly suggested] An email alias of the team from which this dataset product originates. Generally this is the team of the 'dataProductInitialSmeName'.
      - **`dataProductSvcMgmtQueueName`** *(['string'])*: [Optional but strongly suggested] The name of the IT Service Management Incident Queue which would address service problems with the data product--i.e. the ticket queue name for the team which services the data product.  Generally this is the incident queue of the team of the 'dataProductInitialSmeName'.
      - **`systemInitialSmeName`** *(['string'])*: [Optional] The name of the system engineer engaged during the initial data onboarding request, modification, or review.  This individual is only considered to be System SME during the initial onboarding and generally does not have strong familiarity with the dataset itself. If the 'data product team' and 'system team' are the same, omit this property.  In cases where the 'dataProductInitialSmeName' is not responsible for the configuration of the system from which the data originates, this property should be included.
      - **`systemEmailDistributionName`** *(['string'])*: [Optional] If the 'data product' team is not accountable for the management of the system from which the data product originates, this is the email distribution list of the team that manages the underlying system. If the 'data product team' and 'system team' are the same, omit this property.
      - **`systemSvcMgmtQueueName`** *(['string'])*: [Optional] If the 'data product' team is not accountable for the management of the system from which the data product originates, this is the IT Service Management Incident Queue of the team that manages the underlying system. If the 'data product team' and 'system team' are the same, omit this property.
      - **`sourcetypeName`** *(['string'], required)*: The name of the Splunk sourcetype for the dataset. Note: The sourcetype name is not necessarily distinct to this dataset.  If 'indexName'+'sourcetypeName is not distinct, add the 'sourceName' property if that helps with distinctness.  If all 3 do not provide a distinct way to identify the data, consider adding 'notableConsumer' data on an existing data contract's dataset instead of creating a new splunkDataset data contract.
      - **`sourceName`** *(['string'])*: [Optional] Use only if the index:sourcetype combination is not sufficiently distinct for the dataset. Can contain wildcards.
      - **`wineventlog`** *(['object'])*: [Optional Node] [EXPERIMENTAL] Optional - Used only if 'ingestTypeCode' is 'wineventlog'. An object whose properties describe parameters unique to wineventlog inputs.  The 'channel' of the wineventlog events ingested should be recorded in 'sourceName'. Cannot contain additional properties.
        - **`allowedEventCodes`** *(['array'])*: [Optional] If the events in the datasource are to be filtered as allowed by eventCode, list those that are 'allowed' here. Either list criteria individually (i.e. '4543'), as a range or series of ranges '4000-5000', or as a regex expression. This field supports what is allowed in the inputs.conf 'allowList'. Length must be at least 1.
          - **Items** *(['integer', 'string'])*
        - **`deniedEventCodes`** *(['array'])*: [Optional] If the events in the datasource are to be filtered as denied by eventCode, list those that are 'denied' here. Either list criteria individually (i.e. '4543'), as a range or series of ranges '4000-5000', or as a regex expression. This field supports what is allowed in the inputs.conf 'denyList'. Length must be at least 1.
          - **Items** *(['integer', 'string'])*
      - **`indexName`** *(['string'], required)*: The Splunk index into which this dataset is written.
      - **`ingestTypeCode`** *(['array'], required)*: An array of Splunk data ingestion pattern(s) (or ingest types) by which this data is ingressed.
        - **Items**: Must be one of: `["filemon:monitor", "filemon:batch", "winregmon", "syslog", "snmp:trap", "snmp:custom_poller", "wineventlog", "perfmon", "splunkbase add-on", "custom add-on", "hec:on-prem", "hec:cloud", "kafka", "dbconnect", "scripted input", "stream"]`.
      - **`retention`** *(['object'], required)*: Defines the duration of time for searchability and retention of the Splunk dataset--and related policies for extended retention.  If the 'searchableDayCount' is 92 days or less, the other properties in this object should be omitted. Cannot contain additional properties.
        - **`searchableDayCount`** *(['integer'], required)*: The number of days the data will be searchable in Splunk. This correlates directly to the searchable settings for the index into which the data is ingested.  If the 'searchableDayCount' is 92 days or less, the other properties in this object should be omitted. Must be one of: `[2, 8, 14, 30, 60, 90, 92, 180, 366, 397]`.
        - **`retentionDayCount`** *(['integer'])*: [Required when 'searchableDayCount' > 92] The total number of days the data needs to be retained (i.e. the sum of time the dataset is considered both searchable and archived). This correlates directly to the searchable and archival settings for the index into which the data is ingested.  If 'searchableDayCount' is 92 days or less, this value should be omitted.  This is usually dictated by compliance or legislative requirement and, if so, is governed by Enterprise Security Standards Logging. Must be one of: `[2, 8, 14, 30, 60, 92, 180, 366, 397, 1096, 1827, 2192, 2557]`.
        - **`policyVersionNumber`** *(['string', 'number'])*: [Required when 'searchableDayCount' > 92] Identifies the version of the [Enterprise Security Standards Logging] policy document used to identify applicable policies.  If 'searchableDayCount' is 92 days or less, this property should be omitted.
        - **`policyId`** *(['array'])*: [Required when 'searchableDayCount' > 92] An array of the specific logging policy numbers applicable to the dataset's retention (e.g. `7.2`, `8.1.b`, or `3.1`). If 'searchableDayCount' is 92 days or less, this property should be omitted. Length must be at least 1.
          - **Items**
      - **`dataProtection`** *(['object'], required)*: An object whose properties define the dataset's Data Protection Classification and should, by extension, define the access within Splunk. Cannot contain additional properties.
        - **`infoSecClassificationName`**: Identifies the data protection category of the dataset...which in turn identifies the expected level of access to the dataset in Splunk. A dataset having a confidential or higher categorization cannot reside in an un-restricted Splunk index. Must be one of: `["limited use", "confidential", "confidential highly sensitive"]`. Default: `"confidential"`.
        - **`policyVersionNumber`** *(['string', 'number'], required)*: Identifies the version of the Enterprise Security Data Protection policy document used to classify the dataset.
      - **`dataObservability`** *(['object'], required)*: [EXPERIMENTAL] Service Level Objective thresholds and parameters relevent to measuring the quality of the data product. Cannot contain additional properties.
        - **`freshness`** *(['object'], required)*: [EXPERIMENTAL] Data freshness, sometimes referred to as data timeliness, is the maximum expected frequency within which events are to be ingested into Splunk. Cannot contain additional properties.
          - **`measureTypeCode`**: The type of freshness measurement required for this data product. Must be one of: `["host", "indexName:sourcetypeName", "not monitored"]`.
          - **`latencyThresholdName`**: The alert threshold for the data product. For example, if no data is ingested for this entity within the threshold time specified, with some allowable buffer, raise an alert.  Non machine-generated datasets that are transient and unpredictable by nature, should have 'measureTypeCode' set to 'not monitored' and this property omitted. Must be one of: `["5min", "1hour", "12hour", "24hour", "7day"]`.
        - **`projectedVolume`** *(['object'])*: [EXPERIMENTAL] An object containing initial estimates of daily data product storage requirements and event volumes. This element is not expected to be regularly updated, but rather serves as a record to capture initial estimates that can later be compared to actual volumes.  If 'measuredVolume' is available, omit this node. Cannot contain additional properties.
          - **`volumeProjectionDate`**: The date (YYYY-MM-DD) when volume estimates for this data product were made or last revised.
          - **`dailyGbCount`** *(['integer', 'number'], required)*: The projected average daily total gigabytes of data from the data product.
          - **`dailyEventCount`** *(['integer'], required)*: The projected average daily number of events from the data product.
          - **`avgEventByteCount`** *(['integer'])*: The projected average number of bytes per event within the data product.
        - **`measuredVolume`** *(['object'])*: [EXPERIMENTAL] An object containing actual volume measurements of daily data product storage and event volumes. This element is NOT expected to be regularly updated, but rather serves as a record of measurements at a point in time.  This is most useful for recording volumes of datasets that are having data contracts created for them after they were initially ingested.  This is also not intended to be updated to provide historical growth record as that can be pulled via system queries.  If only projected volumes are available, omit this node. Cannot contain additional properties.
          - **`volumeMeasureDate`**: The date (YYYY-MM-DD) when volume estimates for this data product were initially made or last revised because of expected volume changes.
          - **`dailyGbCount`** *(['integer', 'number'], required)*: The observed average daily total gigabytes of data from the data product.
          - **`dailyEventCount`** *(['integer'], required)*: The observed average daily number of events from the data product.
          - **`avgEventByteCount`** *(['integer'])*: [Optional] The observed average number of bytes per event within the data product.
      - **`notableConsumer`** *(['array'])*: [Optional Node] [EXPERIMENTAL] An object providing details on notable consumers who are other than the data product team.  For example, IT Security is the dataSteward of WinEventLog:Security, but there are consumers of specific EventCodes that are outside of that domain.  Capturing 'notableConsumer' information helps record when other parties have requested, or are otherwise known to have a critical dependency upon events that are within the stewardship of another.  This is NOT intended to be a comprehensive list of all consumers of a datset, but only to record when a consumer's needs are tightly coupled to the ingestion requirements for exceptional reasons which could not reasonably be assessed through audit log analysis. Length must be at least 1.
        - **Items** *(['object'])*: Cannot contain additional properties.
          - **`consumer`** *(['object'])*: An object containing elements that describes the notableConsumer and use cases matching specific criteria within the dataset. Cannot contain additional properties.
            - **`consumerName`** *(['string'], required)*: The name or email alias of the team utilizing the events matched by the 'searchCriteriaText'.
            - **`searchCriteriaText`** *(['string'])*: A snippet of SPL search code that identifies the consumed events (e.g. 'EventCode IN (5002 5003)').  If the 'consumer' utilizes the entire dataset, omit this property. Default: `"SPL search criteria....Omit this property if the whole dataset is used by the consumer"`.
            - **`consumerUseCaseDescription`** *(['string'], required)*: For this notable consumer, the value proposition of the events in this data product. Note: For sensitive use cases (i.e. investigative purposes) only note 'Investigative. Purpose not divulged'.
## Examples

  ```yaml
  businessDomainName: Data Engineering
  collectionName: Hadoop Logs
  datasets:
  -   splunkDataset:
          quantumName: apache_projects:apache:hive:logs
          dataContractId: 576b1c04-a8d3-4b83-b62a-bcbc4eae2618
          datasetDescription: Logfiles related to Apache Hive within the Hadoop environment
          datasetStatusCode: proposed
          datasetTypeCode: event
          purposeDescription: To provide alerting opportunities and visibility into
              the Hive application state by consolidating logs into Splunk.
          consumptionModeCode: operational
          dataProductInitialSmeName: Penelope P. Buttercup
          dataProductEmailDistributionName: hive_engineering_team@pwny.com
          dataProductSvcMgmtQueueName: Hive Engineering
          systemInitialSmeName: Nellie T. Elephant
          systemEmailDistributionName: data_eng_ops@pwny.com
          systemSvcMgmtQueueName: Data Eng Operations
          associatedProduct:
          -   product:
                  manufacturerName: Koinpurse Inc.
                  productName: CryptoCurrent Kaleidoscope
          -   product:
                  manufacturerName: Trade Automate Ltd.
                  productName: TradeStreamer
          sourcetypeName: apache:hive:logs
          indexName: apache_projects
          retention:
              searchableDayCount: 366
              retentionDayCount: 1827
              policyId:
              - '2.6'
              - '2.7'
              policyVersionNumber: 4.2.0
          dataProtection:
              infoSecClassificationName: limited use
              policyVersionNumber: 7.0.0
              dpSecurityReviewId: 48
          dataObservability:
              freshness:
                  measureTypeCode: host
                  latencyThresholdName: 1hour
              projectedVolume:
                  volumeProjectionDate: '2023-11-22'
                  dailyGbCount: 15
                  dailyEventCount: 452354
                  avgEventByteCount: 2500
          ingestTypeCode:
          - hec:cloud
          - filemon:monitor
          notableConsumer:
          -   consumer:
                  consumerName: Real Estate
                  searchCriteriaText: EventCode IN (3423 4764)
                  consumerUseCaseDescription: To assiste in identifying users that are
                      physically logging onto the network from an in-office location
          -   consumer:
                  consumerName: HR Investigations
                  searchCriteriaText: EventCode IN (2414 2462)
                  consumerUseCaseDescription: Investigative. Purpose not divulged
          -   consumer:
                  consumerName: data_engineering <data_engineering@pwny.com>
                  consumerUseCaseDescription: For troubleshooting issues that may be
                      experienced as hive is used as data consumer.
  ```


