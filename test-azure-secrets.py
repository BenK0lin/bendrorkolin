# test_secrets.py
# WARNING: This is a test file containing fake Azure credentials for secret scanning tool testing

import os
from datetime import datetime

# Hardcoded connection string
AZURE_STORAGE_CONNECTION = "DefaultEndpointsProtocol=https;AccountName=fakestorageaccount;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;EndpointSuffix=core.windows.net"

# Access token in a variable
access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImtpZCI6IjEyMzQ1Njc4OTAifQ.eyJhdWQiOiJodHRwczovL21hbmFnZW1lbnQuYXp1cmUuY29tIiwiaXNzIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvZmFrZS10ZW5hbnQtaWQvIiwiaWF0IjoxNjE2MTUxNjE2LCJuYmYiOjE2MTYxNTE2MTYsImV4cCI6MTYxNjE1NTUxNn0.THIS_IS_A_FAKE_SIGNATURE_FOR_TESTING_123456789"

class AzureConfig:
    def __init__(self):
        # Service principal credentials in class
        self.client_id = "fake-client-id-123"
        self.client_secret = "Fake8Q~test123secretkeyforazureserviceprincipalABCDEF789"
        self.tenant_id = "fake-tenant-id-456"

    def get_sas_token(self):
        # SAS token in a method
        return "?sv=2021-06-08&ss=bfqt&srt=sco&sp=rwdlacupitfx&se=2024-12-31T21:15:28Z&st=2024-01-01T13:15:28Z&spr=https&sig=FAKE9mhLUv05q2anJCyLeCYy1YhgihSNUboaHqWaGbg%3D"

def initialize_registry():
    # Registry credentials in a function
    registry_password = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDcxNTE2MTYsImlzcyI6ImZha2UtY29udGFpbmVyLXJlZ2lzdHJ5IiwiYXVkIjoiZmFrZS1jb250YWluZXItcmVnaXN0cnkifQ.FAKE_SIGNATURE_FOR_TESTING_PURPOSES_ONLY_123"
    registry_url = "fake-registry.azurecr.io"
    return registry_url, registry_password

# Function key in a dictionary
azure_functions = {
    "function1": {
        "key": "lFakex88Y8xrxcExampleFunctionKeyForTestingPurposesOnly123456789",
        "url": "https://fake-function.azurewebsites.net"
    }
}

# Management certificate in a multiline string
CERT = """MIICiTCCAfKgAwIBAgIQEXAMPLEFAKECERTIFICATEMSFTw="""

# Comments containing secrets (some scanners should detect these)
# Azure Storage: DefaultEndpointsProtocol=https;AccountName=fakestorageaccount2;AccountKey=dGhpcyBpcyBhIGZha2Uga2V5IGZvciBzY2FubmluZyB0ZXN0cyBvbmx5;EndpointSuffix=core.windows.net
# Token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmYWtlIjoidGhpcyBpcyBhIGZha2UgdG9rZW4ifQ.THIS_IS_ANOTHER_FAKE_SIGNATURE_123

def main():
    config = AzureConfig()
    registry_url, registry_pass = initialize_registry()
    
    print("Test application initialized with fake credentials")
    print(f"Registry URL: {registry_url}")
    # This line logs a secret - should be detected
    print(f"Registry password: {registry_pass}")

if __name__ == "__main__":
    main()
