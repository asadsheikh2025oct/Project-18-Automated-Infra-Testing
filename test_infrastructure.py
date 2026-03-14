import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.storage import StorageManagementClient

def test_storage_is_secure():
    credential = DefaultAzureCredential()
    # Use your actual subscription ID
    client = StorageManagementClient(credential, "f2f1d6df-9422-48cb-abf1-0a4eb095ad4a")
    
    # Update these to match your YML values
    account = client.storage_accounts.get_properties("project18", "sttesting202603140000")
    
    # This will FAIL because Bicep set it to True
    assert account.allow_blob_public_access is False, "Security Violation: Public Access is Enabled!"