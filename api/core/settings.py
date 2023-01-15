import os
from dotenv import dotenv_values
from pathlib import Path

PROJECT_NAME = 'Turbo Barber'

# EXPECTED SCOPES
AUTHENTICATED = 'authenticated'
ADMIN = 'admin'

BACKEND_CORS_ORIGINS = ['http://localhost:7071',
                        'https://turbo-barber-apiv1.azurewebsites.net']

ENV_PATH = Path(__file__).parent.parent / '.env'

# REMOTE ENV
# CONFIG_ENV = {
#                 'CONN_STRING': os.environ['CONN_STRING'],
#               'DB': os.environ['DB']
#               }

# LOCAL ENV
CONFIG_ENV = {
                'CONN_STRING': dotenv_values(ENV_PATH)['CONN_STRING'],
              'DB': dotenv_values(ENV_PATH)['DB']
              }

CONN_STRING = CONFIG_ENV['CONN_STRING']
