# Azure Monitor Alert for Public Blob Access Attempts

## 1. Objective

Create an Azure Monitor alert rule to detect anonymous requests attempting to access blob files in an Azure Storage Account. Configure an email notification through an Action Group and document the testing and troubleshooting process.

## 2. Create an Action Group

Before creating the alert rule, I created an Action Group in Azure Monitor.

**Action Group Configuration:**

- **Subscription:** Azure for Students
- **Resource Group:** `ezitech-cloud-intern`
- **Action Group Name:** `PublicBlobAccessActionGroup`
- **Action Type:** Email
- **Email Address:** karbozayb208@gmail.com

The Action Group is responsible for sending email notifications whenever the alert rule is triggered.

## 3. Write a Kusto Query (KQL)

Kusto Query Language (KQL) query to identify anonymous blob requests returning an HTTP 404 status code.

**Initial Query:**

```kusto
StorageBlobLogs
| where StatusCode == 404
| where AuthenticationType == "Anonymous"
```

**Query Explanation:**

- `StorageBlobLogs`: Retrieves blob storage request logs.
- `StatusCode == 404`: Filters requests returning HTTP 404 (Not Found).
- `AuthenticationType == "Anonymous"`: Filters requests made without authentication.

**Reason for Initially Using HTTP 404 Instead of HTTP 403**

I initially used HTTP 404 because, despite trying more than a dozen times with anonymous blob requests and `curl`, I consistently received HTTP 404 instead of the expected HTTP 403 from my private container. Therefore, I temporarily configured the alert rule to detect 404 responses so I could continue testing. Later, after further investigation, I successfully generated HTTP 403 and updated the alert rule accordingly.

## 4. Create an Azure Monitor Alert Rule

After preparing the KQL query and Action Group, I created an Azure Monitor alert rule.

**Alert Rule Configuration:**

- **Alert Rule Name:** `PublicBlobAccessAttempt`
- **Signal Type:** Log Search
- **Condition:** KQL query
- **Initial Status Code:** 404
- **Threshold:** 1
- **Action Group:** `PublicBlobAccessActionGroup`
- **Resource Group:** `ezitech-cloud-intern`

<img width="1361" height="257" alt="image" src="https://github.com/user-attachments/assets/706d507c-4dc9-4db2-a0e4-175d6f32afc8" />


## 5. Initial Testing and Investigation

1. Disabled public access at the container level while keeping Storage Account public access enabled.
2. Sent anonymous requests to access the blob file.
3. Expected HTTP 403 but consistently received HTTP 404, even after more than a dozen attempts using `curl`.

<img width="1135" height="232" alt="image" src="https://github.com/user-attachments/assets/78fe311d-0893-4dc0-9616-39f006917ea5" />

5. Verified the storage account, container, and blob locations.
6. Temporarily enabled container public access and confirmed that the blob contents were accessible through a browser.

<img width="1067" height="465" alt="image" src="https://github.com/user-attachments/assets/959bb33d-45d9-4d5c-84e0-72fe1f7b2da6" />




## 6. Further Investigation: HTTP 403

After researching the issue, I tested by blocking my own public IP address through Storage Account networking.

1. Blocked my public IP address.
2. Requested the blob file again.
3. Received the expected **HTTP 403 (Forbidden)** response.

<img width="778" height="458" alt="image" src="https://github.com/user-attachments/assets/7d887a2b-f860-4754-8fdf-73a023889ab8" />


## 7. Update the Azure Monitor Alert Rule

Updated the KQL query to detect HTTP 403 instead of HTTP 404.

```kusto
StorageBlobLogs
| where StatusCode == 403
| where AuthenticationType == "Anonymous"
```

- **Alert Rule:** `PublicBlobAccessAttempt`
- **Status Code:** 403
- **Threshold:** 1
- **Action Group:** `PublicBlobAccessActionGroup`

## 8. Final Testing and Email Verification

1. Sent another anonymous request while my public IP was blocked.
2. Received HTTP 403.
3. Azure Monitor detected the matching log entry.
4. The alert successfully triggered.
5. Received the email notification through the configured Action Group (Commited in alert.md).

**Final Result:** Successfully tested the Azure Monitor alert and verified email notifications for anonymous requests returning HTTP 403.HTTP 403.

<img width="1237" height="234" alt="image" src="https://github.com/user-attachments/assets/bd8bc95d-e18c-4b85-a596-a1cb6465e1ef" />


## 9. Investigation and Verification (Supervisor's Guidance)

Following my supervisor's advice, I performed an additional investigation to verify the configuration and understand the source of the HTTP 403 response.

I checked the following:

1. **Container Public Access:** Verified the container's public access configuration in Azure. It was set to **Private**, meaning anonymous public access to the container was disabled.
2. **Source IP Address:** Checked the IP address involved in the denied request. It was my own public IP address because I was conducting the alert rule testing.

These checks helped confirm that the container was private and that the denied request originated from my own testing activity.

## 10. Testing Results Summary

| Test Scenario | Result |
|---|---|
| Private container, public IP not blocked | HTTP 404 observed |
| Public access enabled on container | Blob successfully accessible |
| Own public IP blocked at Storage Account level | HTTP 403 observed |
| Alert rule updated from 404 to 403 | Successfully updated |
| Anonymous request repeated after update | HTTP 403 |
| Azure Monitor alert triggered | Successful |
| Email notification received | Successful |
| Container public access investigated | Private |
| Source IP investigated | My own public IP address |

## 11. Security Purpose

This configuration provides monitoring for anonymous blob requests that are denied with HTTP 403 responses.

It helps administrators identify denied access attempts, investigate possible unauthorized requests, and receive email notifications when matching events occur.

**Investigation Conclusion:** Following my supervisor's guidance, I verified that the container was private and that the source IP address belonged to my own testing environment. This helped establish the context of the 403 response and distinguish my authorized testing activity from an unknown external access attempt.

