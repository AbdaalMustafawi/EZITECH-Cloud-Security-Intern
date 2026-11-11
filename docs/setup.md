# Project Setup

Documentation and setup instructions for the Azure Storage project.


1)Firstly I **installed azure CLI** to create storage account before that I register my self to azure student account.
Then:
  Check installation: az --version
  Login to account: az --login --use-device-code
  Check account subscribtion: az account show
  
2)Now have to **create storage account** before that I created a resourse group by using below command chosing the origin **entralindia**: 
  Created a resourse group: az group create --name ezitech-cloud-intern --location centralindia
  Confirm created resourse group: az group show --name ezitech-cloud-intern --output table
Then:
  created storage account: az storage account create --ezitechdeliverylogs2026 --resource-group ezitech-cloud-intern --location             centralindia.
  
3) **Blob Container Creation**:
          az storage container create --name delivery-logs --account-name ezitechdeliverylogs2026 --auth-mode login

4) Storage Logging Configuration

  Enabled Azure Storage logging to monitor read, write, and delete operations.

  **Result:** Storage logging configured for the project. screenshot of logging enabled is attached.
   
5) **Created repo** in my GitHub account then recommended files and Upload.
   
