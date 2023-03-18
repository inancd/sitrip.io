from .base import *

ALLOWED_HOSTS = ['sitrip.io', 'www.sitrip.io', '64.226.84.119', 'localhost']

STATIC_ROOT = "/home/innolove/sitrip.io/static"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
    }
}