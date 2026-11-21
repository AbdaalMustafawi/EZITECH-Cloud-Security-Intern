# Azure Storage Security Audit – Remediation and Verification
**Formatted and Structured by ChatGPT** 
## 1. Introduction

In this phase of the project, we remediated the security findings identified during our previous Azure Storage Account security audit using ScoutSuite.

Our main objectives were:

- Disable public access at the storage container level.
- Disable public blob access at the storage account level.
- Verify that Microsoft-managed encryption keys are enabled.
- Create a test user in Microsoft Entra ID.
- Create a custom read-only role and assign it to the test user.
- Run ScoutSuite again to verify the security improvements.

---

## 2. Remediation of Public Access

### Step 1: Log in to Azure

First, we logged in to our Azure account using the device code authentication method in PowerShell.

```powershell
az login --use-device-code
```

This command provides a device code that we use to authenticate our Azure account through a browser.

### Step 2: Disable Public Access at the Container Level

Next, we disabled public access on our storage container using the following command:

```powershell
az storage container set-permission `
    --name delivery-logs `
    --account-name ezitechdeliverylogs2026 `
    --public-access off `
    --auth-mode login
```

**Explanation:**

- `--name`: Specifies the name of our storage container.
- `--account-name`: Specifies our Azure Storage Account name.
- `--public-access off`: Disables anonymous public access to the container.
- `--auth-mode login`: Uses our authenticated Azure login.

This ensures that users cannot access the container anonymously.

### Step 3: Disable Public Blob Access at the Storage Account Level

After disabling public access at the container level, we also disabled public blob access at the entire storage account level.

We used the following command:

```powershell
az storage account update `
    --resource-group ezitech-cloud-intern `
    --name ezitechdeliverylogs2026 `
    --allow-blob-public-access false
```

**Explanation:**

- `--resource-group`: Specifies our Azure resource group.
- `--name`: Specifies our storage account.
- `--allow-blob-public-access false`: Prevents public blob access at the storage account level.

This provides an additional security layer by preventing containers within the account from allowing anonymous public access.

---
**Screenshots**
<img width="1028" height="309" alt="image" src="https://github.com/user-attachments/assets/8a292f09-a1a7-40ad-a835-a058be0c6307" />





## 3. Verify Microsoft-Managed Encryption Keys

Our second remediation task was to verify that Microsoft-managed encryption keys were enabled for our Azure Storage Account.

Azure Storage uses Microsoft-managed keys by default.

We used the following command:

```powershell
az storage account show `
    --name ezitechdeliverylogs2026 `
    --resource-group ezitech-cloud-intern `
    --query encryption
```

**Explanation:**

- `az storage account show`: Retrieves the storage account configuration.
- `--name`: Specifies our storage account.
- `--resource-group`: Specifies our resource group.
- `--query encryption`: Displays the encryption configuration.

We checked the returned configuration to verify that encryption was enabled and that Microsoft-managed keys were being used.

No additional encryption configuration was required because Microsoft-managed encryption was already enabled.

---
**Screenshots**

<img width="561" height="395" alt="image" src="https://github.com/user-attachments/assets/f08ac3a3-ca97-4e94-8d0e-dde873669995" />

## 4. Create a Test User in Microsoft Entra ID

To test role-based access control (RBAC), we created a separate test user in Microsoft Entra ID.

We followed these steps:

1. Opened the Microsoft Azure Portal.
2. Navigated to **Microsoft Entra ID**.
3. Selected **Users**.
4. Clicked **New user**.
5. Selected **Create new user**.
6. Entered the username `Test-reader`.
7. Set a password.
8. Reviewed the information and created the user.

After creating the user, we obtained its Object ID, which was required for the role assignment.

---
**Screenshots**

<img width="641" height="343" alt="image" src="https://github.com/user-attachments/assets/6bfcc7de-948f-4b21-bd6a-854b9b5ba8af" />


## 5. Create a Custom Read-Only Role

Next, we created a custom Azure RBAC role to provide read-only access to the storage container and its blobs.

### Step 1: Create the JSON Role Definition File

Inside our project repository, we created a file named:

`read-blob-role.json`

We added the following role definition:

```json
{
  "Name": "test-reader",
  "IsCustom": true,
  "Description": "Read-only access to storage containers and blobs.",
  "Actions": [
    "Microsoft.Storage/storageAccounts/blobServices/containers/read"
  ],
  "DataActions": [
    "Microsoft.Storage/storageAccounts/blobServices/containers/blobs/read"
  ],
  "NotActions": [],
  "NotDataActions": [],
  "AssignableScopes": [
    "/subscriptions/17b18937-87c4-4b7a-8c99-d36babadbffc/resourceGroups/ezitech-cloud-intern"
  ]
}
```

### Step 2: Save the JSON File Using PowerShell

We also used PowerShell to write the JSON content into our file:

```powershell
$json = @'
{
  "Name": "test-reader",
  "IsCustom": true,
  "Description": "Read-only access to storage containers and blobs.",
  "Actions": [
    "Microsoft.Storage/storageAccounts/blobServices/containers/read"
  ],
  "DataActions": [
    "Microsoft.Storage/storageAccounts/blobServices/containers/blobs/read"
  ],
  "NotActions": [],
  "NotDataActions": [],
  "AssignableScopes": [
    "/subscriptions/17b18937-87c4-4b7a-8c99-d36babadbffc/resourceGroups/ezitech-cloud-intern"
  ]
}
'@

Set-Content -Path ".\read-blob-role.json" -Value $json -Encoding UTF8
```

**Explanation:**

- `Name`: Defines the custom role name.
- `Actions`: Specifies management-plane permissions to read container information.
- `DataActions`: Specifies permission to read blob data.
- `NotActions` and `NotDataActions`: Define excluded permissions.
- `AssignableScopes`: Specifies the Azure resource scope where this custom role can be assigned.

### Step 3: Create the Custom Role in Azure

After creating the JSON file, we registered our custom role in Azure using:

```powershell
az role definition create --role-definition ".\read-blob-role.json"
```

This command creates the custom RBAC role using our JSON definition.

---

## 6. Assign the Custom Role to the Test User

After successfully creating the custom role, we assigned it to our `Test-reader` user.

We used the following command:

```powershell
az role assignment create `
    --assignee "13655921-69ed-Bac-bf18-ff25332cd9a9" `
    --role "test-reader" `
    --scope "/subscriptions/17b18937-87c4-4b7a-8c99-d36babadbffc/resourceGroups/ezitech-cloud-intern"
```

**Explanation:**

- `az role assignment create`: Creates a new RBAC role assignment.
- `--assignee`: Specifies the Object ID of our test user.
- `--role`: Specifies the custom role we created.
- `--scope`: Specifies where the assigned permissions will apply.

**Understanding the Scope:**

The scope defines the boundary within which a user receives permissions.

In our case, we used the resource group scope. Therefore, the custom role assignment applies to resources within that resource group.

---
**Screenshots**

<img width="986" height="345" alt="image" src="https://github.com/user-attachments/assets/ed80095f-eabf-4e9a-9c9e-23b056d93e16" />


## 7. Run ScoutSuite Security Audit Again

After completing the remediation steps, we performed another security audit using ScoutSuite to check whether our changes had improved the storage account's security.

### Step 1: Activate the Existing Virtual Environment

We navigated to our project directory and activated the virtual environment that we had created during the previous task.

```powershell
.\.venv\Scripts\Activate.ps1
```

This activates our existing Python virtual environment.

### Step 2: Log in to Azure

We authenticated our Azure account again using:

```powershell
az login --use-device-code
```

### Step 3: Run the Second ScoutSuite Scan

After authentication, we executed ScoutSuite again and saved the second audit report inside our repository.

```powershell
scout azure --cli --report-dir docs/audit_2
```

This generated a new security audit report in the `docs/audit_2` directory.

The purpose of this second scan was to verify whether the security improvements made during remediation were reflected in the new audit results.

---

## 8. Second Audit Results and Verification

After completing the second ScoutSuite scan, we reviewed the new security report.

The second scan showed no findings classified as **Critical (red)**.

This indicated that there were no Critical findings displayed in the new audit results.

**Screenshots**

<img width="1177" height="233" alt="image" src="https://github.com/user-attachments/assets/f2354be3-2d47-415c-a8fe-02137cc0aabd" />


<img width="1234" height="240" alt="image" src="https://github.com/user-attachments/assets/440f2977-0636-4dfe-8c72-66d6881ed597" />


### Important Note About the Previous Audit Report

During the previous task, I mistakenly committed security findings that were displayed after selecting the storage account in ScoutSuite without properly checking their severity levels.

I did not distinguish between Critical findings and findings belonging to other severity levels.

As a result, I included findings that were not necessarily Critical in the previous audit documentation.

In this task, I reviewed the severity levels more carefully and understood the importance of distinguishing between different security findings.

---

## 9. Conclusion

In this task, we improved the security configuration of our Azure Storage Account by disabling public access at both the container and storage account levels.

We also verified that Microsoft-managed encryption keys were enabled, created a test user in Microsoft Entra ID, developed a custom read-only RBAC role, and assigned it to the test user.

Finally, we performed a second ScoutSuite security audit to verify our remediation efforts.

The second audit showed no Critical (red) findings, demonstrating an improvement in the reported security posture of our storage account.

**Project:** EZITECH Cloud Security Internship  
**Tool:** Microsoft Azure and ScoutSuite  
**Environment:** PowerShell and Python Virtual Environment
