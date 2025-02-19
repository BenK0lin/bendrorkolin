# Mock Azure Configuration File
# WARNING: These are fake tokens for testing/documentation purposes only

class AzureConfig:
    # Azure Active Directory
    AAD_APP_SECRET = "APP_SECRET~abcd1234-ef56-gh78-ij90-klmnopqrstuv"  # Application secret
    AAD_USER_CRED = "uid=alice@contoso.com;pwd=ExamplePass123!"  # User credential
    
    # Azure API Management
    APIM_DIRECT_KEY = "directmanagement-8a4c2b1e9d3f7g5h"  # Direct management key
    APIM_GATEWAY_KEY = "gateway-p9f8e7d6c5b4a3g2h1"  # Gateway key
    APIM_REPO_KEY = "repository-h2g1f3e4d5c6b7a8p9"  # Repository key
    APIM_SUB_KEY = "23d1b94f86ac5e7h9j2k4m"  # Subscription key
    
    # App Configuration
    APP_CONFIG_CONN = ("Endpoint=https://example-appconfig.azconfig.io;"
                       "Id=l8k7-j6h5-g4f3-d2s1;"
                       "Secret=2z9y8x7w6v5u4t3s")  # App configuration connection string
    
    # Azure Batch
    BATCH_KEY = ("sv=2020-01-01&ss=b&srt=s&sp=rwdl&"
                 "se=2025-01-01T00:00:00Z&st=2024-01-01T00:00:00Z&"
                 "spr=https&sig=batch%2Bkey%example123")  # Batch key
    
    # Azure Cache for Redis
    REDIS_KEY = "redisaccess=zlk4j3h2g1f9d8s7a6"  # Redis access key
    
    # Communication Services
    COMMUNICATION_CONN = ("endpoint=https://example.communication.azure.com/;"
                         "accesskey=1a2b3c4d5e6f7g8h9i0j")  # Communication services connection string
    
    # Container Registry
    CONTAINER_REG_KEY = "registrykey=cr1234567890abcdef"  # Container registry key
    
    # CosmosDB
    COSMOS_KEY = "cosmosdb=7h8j9k0l1m2n3p4q5r"  # CosmosDB key
    
    # Azure DevOps
    DEVOPS_PAT = "pat_v2.0.12345abcdefghijklmnopqrstuvwxyz0123"  # Personal access token
    
    # Event Hub
    EVENT_HUB_KEY = ("Endpoint=sb://example.servicebus.windows.net/;"
                     "SharedAccessKeyName=RootManageSharedAccessKey;"
                     "SharedAccessKey=evhub123456789")  # Event hub key
    
    # Azure Functions
    FUNCTION_KEY = "functionkey=0z9y8x7w6v5u4t3s2r1q"  # Function key
    
    # IoT Configuration
    IOT_DEVICE_CONN = ("HostName=example.azure-devices.net;"
                       "DeviceId=myDevice;"
                       "SharedAccessKey=iotdevice123456")  # IoT device connection string
    IOT_DEVICE_KEY = "iotdevicekey=9q8w7e6r5t4y3u2i1o"  # IoT device key
    IOT_PROVISION_KEY = "provisionkey=2w3e4r5t6y7u8i9o0p"  # IoT device provisioning key
    IOT_HUB_CONN = ("HostName=example.azure-devices.net;"
                    "SharedAccessKeyName=iothubowner;"
                    "SharedAccessKey=iothub123456789")  # IoT hub connection string
    IOT_HUB_KEY = "iothubkey=5t6y7u8i9o0p1a2s3d"  # IoT hub key
    IOT_PROVISION_CONN = ("HostName=example.azure-devices-provisioning.net;"
                         "SharedAccessKeyName=provisioningowner;"
                         "SharedAccessKey=provision123456")  # IoT provisioning connection string
    
    # Management and ML
    MGMT_CERT = "managementcert=mc1234567890abcdef"  # Management certificate
    ML_WEB_SERVICE_KEY = "mlwebservice=mls7h8j9k0l1m2n3p4"  # ML web service classic key
    
    # Azure OpenAI
    OPENAI_KEY = "sk-aoai4k3j2h1g9f8d7s6a5"  # OpenAI key
    
    # Azure Relay
    RELAY_KEY = "relaykey=rk2s3d4f5g6h7j8k9l"  # Relay key
    
    # SAS Token
    SAS_TOKEN = ("sv=2020-01-01&ss=b&srt=s&sp=rwdl&"
                 "se=2025-01-01T00:00:00Z&st=2024-01-01T00:00:00Z&"
                 "spr=https&sig=sas%2Btoken%example123")  # SAS token
    
    # Search Service
    SEARCH_ADMIN_KEY = "searchadmin=sa3f4g5h6j7k8l9p0"  # Search admin key
    SEARCH_QUERY_KEY = "searchquery=sq7g8h9j0k1l2p3m4"  # Search query key
    
    # Service Bus
    SERVICE_BUS_KEY = ("Endpoint=sb://example.servicebus.windows.net/;"
                       "SharedAccessKeyName=RootManageSharedAccessKey;"
                       "SharedAccessKey=servicebus123456")  # Service bus key
    
    # SignalR
    SIGNALR_CONN = ("Endpoint=https://example.service.signalr.net;"
                    "AccessKey=signalr1234567890;"
                    "Version=1.0;")  # SignalR connection string
    
    # SQL Database
    SQL_CONN = ("Server=example.database.windows.net;"
                "Database=mydb;"
                "User ID=admin;"
                "Password=sqlpass123!;")  # SQL connection string
    SQL_PASSWORD = "SqlP@ssw0rd123!"  # SQL password
    
    # Storage Account
    STORAGE_ACCOUNT_KEY = ("DefaultEndpointsProtocol=https;"
                          "AccountName=example;"
                          "AccountKey=storageacc123456==;"
                          "EndpointSuffix=core.windows.net")  # Storage account key
    
    # Web PubSub
    WEB_PUBSUB_CONN = ("Endpoint=https://example.webpubsub.azure.com;"
                       "AccessKey=pubsub123456789;"
                       "Version=1.0;")  # Web PubSub connection string
    
    # Entra ID and Corporate Network
    ENTRA_ID_TOKEN = ("eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IjJaUXBKM"
                      "1VwYmpBWVhZR2FYRUpsOGxWMFRPSSJ9.example")  # Entra ID token
    CORP_NET_CRED = "domain\\username:CorpP@ssw0rd123!"  # Corporate network credential


def get_config():
    """Returns an instance of the AzureConfig class containing mock credentials"""
    return AzureConfig()
