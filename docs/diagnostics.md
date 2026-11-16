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

**Screenshot:**
<img width="1366" height="222" alt="Screenshot 2026-11-16 092948" src="https://github.com/user-attachments/assets/a2820d03-0fa3-4052-b566-4b08de2421a0" />


**Configuration:**

- Resource Group: `ezitech-cloud-intern`
- Workspace Name: `aquafresh-logs-workspace`
- Region: `Central India`
- Data Retention: `30 Days`

## 2. Configure Diagnostic Settings
My Workspace ID:daff00dd-c7b8-4634-bdac-b2b0539731cc

**Command used:** Creates Diagnostic Settings to connect the Azure Storage Blob Service to the Log Analytics Workspace.

```powershell
az monitor diagnostic-settings create `
  --name aquafresh-logs-workspace `
  --resource "/subscriptions/17b10937-87c4-4b7a-8c99-d36babadbffc/resourceGroups/ezitech-cloud-intern/providers/Microsoft.Storage/storageAccounts/ezitechdeliverylogs2026/blobServices/default" `
  --workspace "/subscriptions/17b10937-87c4-4b7a-8c99-d36babadbffc/resourceGroups/ezitech-cloud-intern/providers/Microsoft.OperationalInsights/workspaces/aquafresh-logs-workspace" `
  --logs '[{"category":"StorageRead","enabled":true},{"category":"StorageWrite","enabled":true},{"category":"StorageDelete","enabled":true}]'
```
**Screenshot:**
<img width="1361" height="162" alt="image" src="https://github.com/user-attachments/assets/503593f5-7f87-479b-9ad6-9d1d893d21dd" />

**Enabled Log Categories:**

| Category      | Description                       |
| ------------- | --------------------------------- |
| StorageRead   | Records storage read operations   |
| StorageWrite  | Records storage write operations  |
| StorageDelete | Records storage delete operations |

**Screenshot:**
<img width="1361" height="162" alt="image" src="https://github.com/user-attachments/assets/503593f5-7f87-479b-9ad6-9d1d893d21dd" />

## 3. Verify Storage Logs

After configuring Diagnostic Settings, storage events were generated and forwarded to the Log Analytics Workspace.

**Log Analytics Query:**

```kusto
StorageBlobLogs
| take 100
```
**Screenshot:**
<img width="1009" height="474" alt="image" src="https://github.com/user-attachments/assets/8c9192c9-66fb-4984-afc8-2cf2277c0302" />

## 4. Evidence and Screenshots

The screenshots provided in "create workspace log(1).pdf" and "Task02(screenshots.evedence).pdf" in the docs/ file in this repository demonstrate the successful configuration and verification:

- Log Analytics Workspace creation. https://github.com/user-attachments/assets/625210c0-2130-4a13-8d33-1ac7255365cc
- Diagnostic Settings configuration.
- Storage events visible in Log Analytics query results.
- screenshot of storage events are attached.

## Expected Outcome

- [x] Log Analytics Workspace created.
<img width="1366" height="222" alt="Screenshot 2026-11-16 092948" src="https://github.com/user-attachments/assets/a2820d03-0fa3-4052-b566-4b08de2421a0" />

- [x] Azure Storage Account linked through Diagnostic Settings.
<img width="1361" height="162" alt="image" src="https://github.com/user-attachments/assets/503593f5-7f87-479b-9ad6-9d1d893d21dd" />

- [x] Storage Read, Write, and Delete logging enabled.
<img width="1100" height="642" alt="image" src="https://github.com/user-attachments/assets/5085700a-06cb-41be-9cdc-ab43f2a1bf3c" />

- [x] Storage events visible in Log Analytics query results.
<img width="1009" height="474" alt="image" src="https://github.com/user-attachments/assets/8c9192c9-66fb-4984-afc8-2cf2277c0302" />



**Result:** Azure Storage diagnostic logging is configured to forward storage events to the Log Analytics Workspace for centralized monitoring and analysis.
