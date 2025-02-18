# test_secrets.py
# WARNING: This is a test file containing fake Azure credentials for secret scanning tool testing

import os
from datetime import datetime

# Azure Access Token (JWT)
ACCESS_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImtpZCI6IjEyMzQ1Njc4OTAifQ.eyJhdWQiOiJodHRwczovL21hbmFnZW1lbnQuYXp1cmUuY29tIiwiaXNzIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvZmFrZS10ZW5hbnQtaWQvIiwiaWF0IjoxNjE2MTUxNjE2LCJuYmYiOjE2MTYxNTE2MTYsImV4cCI6MTYxNjE1NTUxNn0.THIS_IS_A_FAKE_SIGNATURE_FOR_TESTING_123456789"

# Storage Connection String
AZURE_STORAGE_CONNECTION = "DefaultEndpointsProtocol=https;AccountName=fakestorageaccount;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;EndpointSuffix=core.windows.net"

# SAS Token
sas_token = "?sv=2021-06-08&ss=bfqt&srt=sco&sp=rwdlacupitfx&se=2024-12-31T21:15:28Z&st=2024-01-01T13:15:28Z&spr=https&sig=FAKE9mhLUv05q2anJCyLeCYy1YhgihSNUboaHqWaGbg%3D"

class AzureConfig:
    def __init__(self):
        # Service Principal Secret
        self.client_secret = "Fake8Q~test123secretkeyforazureserviceprincipalABCDEF789"
        
        # Registry Access Token
        self.registry_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlRFU1QxMjM0In0.eyJqdGkiOiJmYWtlLWp0aS1pZCIsImlhdCI6MTYxNjE1MTYxNiwibmJmIjoxNjE2MTUxNjE2LCJleHAiOjE2MTYxNTU1MTYsImlzcyI6ImZha2UtcmVnaXN0cnkuYXp1cmVjci5pbyIsImF1ZCI6ImZha2UtcmVnaXN0cnkuYXp1cmVjci5pbyJ9.THIS_IS_A_FAKE_SIGNATURE_FOR_TESTING_987654321"

# Function Key in dictionary
azure_functions = {
    "function1": {
        "key": "lFakex88Y8xrxcExampleFunctionKeyForTestingPurposesOnly123456789",
        "url": "https://fake-function.azurewebsites.net"
    }
}

# Management Certificate
MANAGEMENT_CERT = """MIICiTCCAfKgAwIBAgIQEXAMPLEFAKECERTIFICATEMSFTw="""

# Container Registry Password
CONTAINER_REGISTRY_PASSWORD = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDcxNTE2MTYsImlzcyI6ImZha2UtY29udGFpbmVyLXJlZ2lzdHJ5IiwiYXVkIjoiZmFrZS1jb250YWluZXItcmVnaXN0cnkifQ.FAKE_SIGNATURE_FOR_TESTING_PURPOSES_ONLY_123"

def get_storage_credentials():
    # Secrets in function return
    return {
        "connection_string": "DefaultEndpointsProtocol=https;AccountName=fakestorageaccount;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;EndpointSuffix=core.windows.net",
        "sas_token": "?sv=2021-06-08&ss=bfqt&srt=sco&sp=rwdlacupitfx&se=2024-12-31T21:15:28Z&st=2024-01-01T13:15:28Z&spr=https&sig=FAKE9mhLUv05q2anJCyLeCYy1YhgihSNUboaHqWaGbg%3D"
    }

def initialize_services():
    # Multiple secrets in function variables
    access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImtpZCI6IjEyMzQ1Njc4OTAifQ.eyJhdWQiOiJodHRwczovL21hbmFnZW1lbnQuYXp1cmUuY29tIiwiaXNzIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvZmFrZS10ZW5hbnQtaWQvIiwiaWF0IjoxNjE2MTUxNjE2LCJuYmYiOjE2MTYxNTE2MTYsImV4cCI6MTYxNjE1NTUxNn0.THIS_IS_A_FAKE_SIGNATURE_FOR_TESTING_123456789"
    registry_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlRFU1QxMjM0In0.eyJqdGkiOiJmYWtlLWp0aS1pZCIsImlhdCI6MTYxNjE1MTYxNiwibmJmIjoxNjE2MTUxNjE2LCJleHAiOjE2MTYxNTU1MTYsImlzcyI6ImZha2UtcmVnaXN0cnkuYXp1cmVjci5pbyIsImF1ZCI6ImZha2UtcmVnaXN0cnkuYXp1cmVjci5pbyJ9.THIS_IS_A_FAKE_SIGNATURE_FOR_TESTING_987654321"
    client_secret = "Fake8Q~test123secretkeyforazureserviceprincipalABCDEF789"
    
    print(f"Initialized with token: {access_token}")  # Logging secrets - should be detected

# Comments containing secrets (some scanners should detect these)
# Access Token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImtpZCI6IjEyMzQ1Njc4OTAifQ.eyJhdWQiOiJodHRwczovL21hbmFnZW1lbnQuYXp1cmUuY29tIiwiaXNzIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvZmFrZS10ZW5hbnQtaWQvIiwiaWF0IjoxNjE2MTUxNjE2LCJuYmYiOjE2MTYxNTE2MTYsImV4cCI6MTYxNjE1NTUxNn0.THIS_IS_A_FAKE_SIGNATURE_FOR_TESTING_123456789
# Cert: MIICiTCCAfKgAwIBAgIQEXAMPLEFAKECERTIFICATEMSFTw=

def main():
    config = AzureConfig()
    creds = get_storage_credentials()
    initialize_services()
    
    print("Test application initialized with fake credentials")

if __name__ == "__main__":
    main()
