import os


# Cloud API Keys
API_KEY = os.getenv('API_KEY',None)
API_SECRET_KEY = os.getenv('API_SECRET_KEY',None)
BOOTSTRAP_SERVER = os.getenv('BOOTSTRAP_SERVER',None)
# Schema keys
SCHEMA_REGISTRY_API_KEY = os.getenv('SCHEMA_REGISTRY_API_KEY',None)
SCHEMA_REGISTRY_API_SECRET = os.getenv('SCHEMA_REGISTRY_API_SECRET',None)
ENDPOINT_SCHEMA_URL = os.getenv('ENDPOINT_SCHEMA_URL',None)
# Security and SSL
SECURITY_PROTOCOL = os.getenv('SECURITY_PROTOCOL',None)
SSL_MACHENISM = os.getenv('SSL_MACHENISM',None)


def sasl_conf():
    sasl_conf = {
        'sasl.mechanism': SSL_MACHENISM,
        'bootstrap.servers': BOOTSTRAP_SERVER,
        'security.protocol': SECURITY_PROTOCOL,
        'sasl.username': API_KEY,
        'sasl.password': API_SECRET_KEY
    }
    return sasl_conf

def schema_config():
    return{
        'url': ENDPOINT_SCHEMA_URL,
        'basic.auth.user.info': f"{SCHEMA_REGISTRY_API_KEY}:{SCHEMA_REGISTRY_API_SECRET}"
    }

if __name__ == '__main__':
    sasl_conf()
    