"""
Django settings for jubside project.

Generated by 'django-admin startproject' using Django 1.11.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from easy_thumbnails.conf import Settings as EasyThumbnailSettings

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SITE_ID = 1
ALLOWED_HOSTS = ["127.0.0.1", "localhost", "jubside.nabla.no"]

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ff34xtnmhg8uc3er$=q@y1lk2w^*m^ta7(1qf0diz#hbw62ays'


LOGIN_REDIRECT_URL = '/min-profil/'

# Gjør det enkelt å bruke relative paths
PROJECT_ROOT = os.path.join(os.path.dirname(__file__), "..", "..")
VARIABLE_CONTENT = os.environ.get("VARIABLE_CONTENT", os.path.join(PROJECT_ROOT, 'var'))

# Absolute path to the directory that holds media.
MEDIA_ROOT = os.path.join(VARIABLE_CONTENT, 'media')
MEDIA_URL = '/media/'

STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'


# Application definition
INSTALLED_APPS = [
    # Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.flatpages',
    'django.contrib.humanize',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',

    # Self-made
    'content',
    'contentapps.album',
    'events',
    'jubside',
    'user',

    # Django-packages
    'bootstrap3',
    'easy_thumbnails',
    'image_cropping',
    'sekizai',
    'qr_code',
    'naomi',
]

AUTH_USER_MODEL = 'user.User'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Custom session cookie
SESSION_COOKIE_NAME = 'jubsess_id'

ROOT_URLCONF = 'jubside.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'sekizai.context_processors.sekizai',
            ],
        },
    },
]

WSGI_APPLICATION = 'jubside.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        }
}

# All epost blir åpnet i nettleseren og lagret som en html-fil, istedet for å sendes ut til brukerne.
# EMAIL_BACKEND = "naomi.mail.backends.naomi.NaomiBackend"

# EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_FILE_PATH = os.path.join(VARIABLE_CONTENT, 'email')

# easy_thumbnail debugging
# Gjør at man får en feilmelding dersom thumbnail-taggen ikke klarer å lage ny
# thumbnail
THUMBNAIL_DEBUG = True

# easy-thumbnails/Django-image-cropping
THUMBNAIL_PROCESSORS = (
    'image_cropping.thumbnail_processors.crop_corners',
) + EasyThumbnailSettings.THUMBNAIL_PROCESSORS
THUMBNAIL_BASEDIR = 'thumbnails'

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

if DEBUG:
    AUTH_PASSWORD_VALIDATORS = []


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/


TIME_ZONE = 'Europe/Oslo'
LANGUAGE_CODE = 'nb'
USE_L10N = False
DATE_FORMAT = 'j. F Y'

USE_I18N = True


USE_TZ = False

