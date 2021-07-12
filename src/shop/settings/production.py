from .base import *


# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = False

ALLOWED_HOSTS = ['localhost']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': environ.get('MYSQL_DATABASE', None),
        'USER': environ.get('MYSQL_USER', None),
        'PASSWORD': environ.get('MYSQL_PASSWORD', None),
        'HOST': environ.get('MYSQL_HOST', None), 
        'PORT': '3306'
    },
}

# Application definition

INSTALLED_APPS = DJANGO_APPS + APPS_THIRD_PARTY + APPS

# Email

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mailtrap.io'
EMAIL_HOST_USER = environ.get("DJANGO_EMAIL_HOST_USER", None)
EMAIL_HOST_PASSWORD = environ.get("DJANGO_EMAIL_HOST_PASSWORD", None)
EMAIL_PORT = '2525'