from .base import *

ALLOWED_HOSTS = ['sitrip.io', 'www.sitrip.io', '64.226.84.119']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'innolove',
        'USER': 'myinnolove',
        'PASSWORD': 'noksk1991!',
        'HOST': 'localhost',
        'PORT': '',
    }
}