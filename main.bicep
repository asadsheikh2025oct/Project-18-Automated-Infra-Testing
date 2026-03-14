param location string = 'ukwest'
param storageAccountName string = 'sttesting202603140000'

resource storage 'Microsoft.Storage/storageAccounts@2023-05-01' ={
  name: storageAccountName
  location: location
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
  properties: {
    accessTier: 'Hot'
    allowBlobPublicAccess: true
    supportsHttpsTrafficOnly: false
  }
}
output storageName string = storage.name
