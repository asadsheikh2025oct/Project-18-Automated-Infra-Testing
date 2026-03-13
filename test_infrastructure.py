# test_infrastructure.py snippet
def test_storage_is_secure(storage_client):
    account = storage_client.storage_accounts.get_properties("RG_NAME", "ST_NAME")
    # This will fail if you set allowBlobPublicAccess to True in Bicep
    assert account.allow_blob_public_access is False