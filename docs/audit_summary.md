# Azure Storage Account Security Audit – ScoutSuite

## 1. Overview

This document explains how we performed a security audit of our Azure Storage Account using **ScoutSuite**, identified three security findings, and applied the recommended security improvements.

The main objective was to identify potential security weaknesses and improve the overall security of our Azure Storage Account.

---

## 2. Running the ScoutSuite Security Audit

We used ScoutSuite to scan our Azure environment and identify potential security misconfigurations.

### Step 1: Create a Virtual Environment

First, create a Python virtual environment to install and manage the required dependencies separately.

```powershell
python -m venv .venv
```

### Step 2: Activate the Virtual Environment

Activate the virtual environment using the following command:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Step 3: Log in to Azure

Log in to your Azure account using the Azure CLI:

```powershell
az login --use-device-code
```

### Step 4: Check the Selected Subscription

Verify that the correct Azure subscription is selected:

```powershell
az account show
```

### Step 5: Run the ScoutSuite Security Scan

Run the following command from inside the activated virtual environment and your project repository directory:

```powershell
scout azure --cli --report-dir docs/audit
```

**Expected Result:** ScoutSuite generates an HTML security audit report inside the `docs/audit` directory.

---

## 3. Security Audit Results and Recommended Fixes
**Note:**Detail security audit is commited in docs/audit/ 

After running the ScoutSuite security audit, we identified three important security findings related to aquafresh-logs-workspace in our Azure Storage Account.

### Finding 1: Blob Containers Allowing Public Access

**Risk:**

Publicly accessible blob containers may allow unauthorized users to read exposed storage data without authentication.

**Recommended Fix:**

Disable anonymous blob access to prevent public access to blob containers.

**Steps to Fix:**

1. Open your Azure Storage Account in the Azure Portal.
2. Under **Settings**, select **Configuration**.
3. Find **Allow Blob Anonymous Access**.
4. Set the option to **Disabled**.
5. Click **Save** to apply the changes.

**Security Improvement:**

Disabling anonymous blob access helps prevent unauthorized users from accessing publicly exposed blob data.

**Screenshot:**
<img width="613" height="400" alt="image" src="https://github.com/user-attachments/assets/850bb531-9cd1-417f-bca3-74e42bc15a17" />


### Finding 2: Secure Transfer (HTTPS) Is Not Enforced

**Risk:**

If secure transfer is not enforced, clients may communicate with the storage account over unencrypted HTTP connections. This can expose transmitted information to interception.

**Recommended Fix:**

Enable **Secure Transfer Required** to enforce secure HTTPS connections.

**Steps to Fix:**

1. Open your Azure Storage Account in the Azure Portal.
2. Under **Settings**, select **Configuration**.
3. Find **Secure Transfer Required**.
4. Change the setting to **Enabled**.
5. Click **Save** to apply the changes.

**Security Improvement:**

Enforcing HTTPS protects data in transit by using encrypted communication between clients and the storage account.

**Screenshot:**
<img width="613" height="400" alt="image" src="https://github.com/user-attachments/assets/850bb531-9cd1-417f-bca3-74e42bc15a17" />

### Finding 3: Storage Account Access Key Is Not Rotated

**Risk:**

If a storage account access key is leaked or compromised, an attacker may continue using that key to access the storage account until it is rotated or otherwise invalidated.

**Recommended Fix:**

Regenerate the storage account access key periodically and update applications that depend on it.

**Steps to Fix:**

1. Open your Azure Storage Account in the Azure Portal.
2. Under **Security + networking**, select **Access keys**.
3. Identify the key you want to rotate (**Key1** or **Key2**).
4. Select **Rotate key** or **Regenerate**, depending on the available portal option.
5. Update applications and services that use the regenerated key.

**Important:** Before regenerating an access key, make sure your applications have been updated to use the other valid key. This helps prevent service interruptions.

**Security Improvement:**

Regular key rotation reduces the risk of continued unauthorized access through compromised or outdated access keys.

---
**Screenshot:**
<img width="1003" height="546" alt="image" src="https://github.com/user-attachments/assets/5e09a349-962d-46f6-9c2f-4465deb098e1" />

## 4. Final Security Improvements

The ScoutSuite security audit helped us identify three important security weaknesses in our Azure Storage Account.

The following security improvements were applied:

| No. | Security Finding | Recommended Improvement |
|---|---|---|
| 1 | Blob Containers Allowing Public Access | Disabled anonymous blob access |
| 2 | Secure Transfer Not Enforced | Enabled Secure Transfer Required (HTTPS) |
| 3 | Storage Account Access Key Not Rotated | Rotated the access key and updated dependent applications |

---

## 5. Conclusion

ScoutSuite helped us identify potential security weaknesses and misconfigurations in our Azure Storage Account.

By addressing these findings, we improved storage security, reduced the risk of unauthorized access, enforced encrypted data transmission, and strengthened access key management.

This task provided practical experience with Azure security auditing, ScoutSuite, Azure CLI, and security remediation through the Azure Portal.

**Overall Result:** The identified security issues were addressed, and the Azure Storage Account security configuration was improved.
