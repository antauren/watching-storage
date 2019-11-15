import os

from dotenv import dotenv_values


def is_true(value: str) -> bool:
    return value.strip().lower() == 'true'


ENV = dotenv_values()

DEBUG = is_true(ENV.get('DEBUG', 'False'))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': ENV['HOST'],
        'PORT': ENV['PORT'],

        'NAME': ENV['NAME'],
        'USER': ENV['USER'],
        'PASSWORD': ENV['PASSWORD'],
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = 'REPLACE_ME'

ROOT_URLCONF = "project.urls"

ALLOWED_HOSTS = ['*']

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]

USE_L10N = True

LANGUAGE_CODE = 'ru-ru'
