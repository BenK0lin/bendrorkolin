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
client_secret = 'bP88Q~rcBcYjzzOhg1Hnn76Wm3jGgakZiZ.8vMgR'
# Management Certificate
MANAGEMENT_CERT = """MIICiTCCAfKgAwIBAgIQEXAMPLEFAKECERTIFICATEMSFTw="""

# Container Registry Password
CONTAINER_REGISTRY_PASSWORD = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDcxNTE2MTYsImlzcyI6ImZha2UtY29udGFpbmVyLXJlZ2lzdHJ5IiwiYXVkIjoiZmFrZS1jb250YWluZXItcmVnaXN0cnkifQ.FAKE_SIGNATURE_FOR_TESTING_PURPOSES_ONLY_123"
`client_secret=bP88Q~rcBcYjzzOhg1Hnn76Wm3jGgakZiZ.8vMgR`, // gitleaks:allow
`client_secret=bP88Q~rcBcYjzzOhg1Hnn76Wm3jGgakZiZ.8vMgR
`, // gitleaks:allow
`client_secret: .IQ8Q~79R7TOWOspFnWcEG-dYt4KXqFqxK16cxr`,                                                                                              // gitleaks:allow
		`AUTH_CLIENTSECRET = _V28Q~IC8qxmlWNpHuDm34JlbKv9LXV5MvUR3a-P`,                                                                                        // gitleaks:allow
		`<value xsi:type="xsd:string">~Gg8Q~nVhlLi2vpg_nXBGqFsbGK-t~Hus1JmTa0y</value>`,                                                                       // gitleaks:allow
		`"CLIENT_SECRET": "YYz7Q~Sudoqwap1PnzEBA3zqBK~i5uesDIv.C"`,                                                                                            // gitleaks:allow
		`Set-PSUAuthenticationMethod -Type 'OpenIDConnect' -CallbackPath '/auth/oidc' -ClientId 'fake' -ClientSecret '2Vq7Q~q5VgKljZ7cb3.0sp0Apz.vOjRIPyeTr'`, // gitleaks:allow
		`client-secret: "t028Q~-aLbmQuinnZtzbgtlEAYstnBWEmGPAoBm"`,                                                                                            // gitleaks:allow
		`"cas.authn.azure-active-directory.client-secret=qHF8Q~PCM5HhMoyTFc5TYEomnzR6Kim9UJhe8a.P",`,                                                          // gitleaks:allow
		`"line": "client_srt = \"qpF8Q~PCM5MhMoyTFc5TYEomnYRUKim9UJhe8a2P\";",`,                                                                               // gitleaks:allow
		`"client_secret":       acctest.Representation{RepType: acctest.Required, Create: 'dO29Q~F5-VwnW.lZdd11xFF_t5NAXCaGwDl9NbT1'},`,                       // gitleaks:allow
		`Example= GN.7Q~4AkLZBNEbz4Jxlm~O5G6SsyFxYg6zMR`,                                                                                                      // gitleaks:allow
		`"the_value": "QtT8Q~9C-_Ij~RouHVpD2Tuf3oHWGh.DQ3kcjbAn"`,                                                                                             // gitleaks:allow
		`QtT8Q~9C-_Ij~RouHVpD2Tuf3oHWGh.DQ3kcjbAn`,                                                                                                            // gitleaks:allow
		`(use the client secret: QtT8Q~9C-_Ij~RouHVpD2Tuf3oHWGh.DQ3kcjbAn)`,                                                                                   // gitleaks:allow
		`(QtT8Q~9C-_Ij~RouHVpD2Tuf3oHWGh.DQ3kcjbAn)`,                                                                                                          // gitleaks:allow
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
