# Task 02: Configure Azure Diagnostics to Forward Storage Logs to Log Analytics

## Objective

Configure Azure Diagnostic Settings to forward Azure Storage Account logs to an Azure Log Analytics Workspace for centralized monitoring and analysis.

## Requirements

- Create an Azure Log Analytics Workspace.
- Link the Storage Account to the workspace using Diagnostic Settings.
- Enable Storage Read, Write, and Delete logs.
- Verify that storage events are being forwarded to the workspace.
- Confirm at least one log entry is visible in query results.

## 1. Create Log Analytics Workspace

**Command used:** Creates a Log Analytics Workspace in the existing Azure Resource Group.

```powershell
az monitor log-analytics workspace create `
  --resource-group ezitech-cloud-intern `
  --workspace-name aquafresh-logs-workspace `
  --location centralindia `
  --retention-time 30
```

**Configuration:**

- Resource Group: `ezitech-cloud-intern`
- Workspace Name: `aquafresh-logs-workspace`
- Region: `Central India`
- Data Retention: `30 Days`

## 2. Configure Diagnostic Settings

**Command used:** Creates Diagnostic Settings to connect the Azure Storage Blob Service to the Log Analytics Workspace.

```powershell
az monitor diagnostic-settings create `
  --name aquafresh-logs-workspace `
  --resource "/subscriptions/17b10937-87c4-4b7a-8c99-d36babadbffc/resourceGroups/ezitech-cloud-intern/providers/Microsoft.Storage/storageAccounts/ezitechdeliverylogs2026/blobServices/default" `
  --workspace "/subscriptions/17b10937-87c4-4b7a-8c99-d36babadbffc/resourceGroups/ezitech-cloud-intern/providers/Microsoft.OperationalInsights/workspaces/aquafresh-logs-workspace" `
  --logs '[{"category":"StorageRead","enabled":true},{"category":"StorageWrite","enabled":true},{"category":"StorageDelete","enabled":true}]'
```

**Enabled Log Categories:**

| Category      | Description                       |
| ------------- | --------------------------------- |
| StorageRead   | Records storage read operations   |
| StorageWrite  | Records storage write operations  |
| StorageDelete | Records storage delete operations |

## 3. Verify Storage Logs

After configuring Diagnostic Settings, storage events were generated and forwarded to the Log Analytics Workspace.

**Log Analytics Query:**

```kusto
StorageBlobLogs
| take 10
```

## 4. Evidence and Screenshots

The following screenshots demonstrate the successful configuration and verification:

- Log Analytics Workspace creation.
- Diagnostic Settings configuration.
- Storage events visible in Log Analytics query results.

## Expected Outcome

- [x] Log Analytics Workspace created.
- [x] Azure Storage Account linked through Diagnostic Settings.
- [x] Storage Read, Write, and Delete logging enabled.
- [x] Storage events visible in Log Analytics query results.

**Result:** Azure Storage diagnostic logging is configured to forward storage events to the Log Analytics Workspace for centralized monitoring and analysis.
