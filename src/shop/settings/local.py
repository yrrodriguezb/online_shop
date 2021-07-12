from .base import *


# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '0.0.0.0',
    '127.0.0.1',
]

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Application definition

INSTALLED_APPS = DJANGO_APPS + APPS_THIRD_PARTY + APPS


# Email

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'