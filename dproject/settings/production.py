from .base import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []

DATABASES = {
    "default": {
      "ENGINE": "django.db.backends.postgresql_psycopg2",
      "NAME": "twoscoops",
      "USER": "",
      "PASSWORD": "",
      "HOST": "localhost",
      "PORT": "", 
      }
}