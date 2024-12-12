import os 

from ua.settings import *
from ua.settings import BASE_DIR

ALLOWED_HOSTS = 'zenatixproject-hbcmc2b9f3ambph8.centralus-01.azurewebsites.net'
CSRF_TRUSTED_ORIGINS = ['https://' + os.environ.get('ALLOWED_HOSTS')]
DEBUG = False

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

connection_string  = os.environ.get('AZURE_POSTGRESQL_CONNECTIONSTRING')
parameters = {pair.split('='): pair.split('=')[1] for pair in connection_string.split(' ')}



DATABASES = {
    'default': {
        'Server'
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': parameters.get('dbname'),
        'USER': parameters.get('user'),
        'PASSWORD': parameters.get('password'),
        'HOST': parameters.get('host'),
        'PORT': parameters.get('port'),
    }
}


SECRET_KEY = os.environ.get('sceret')
