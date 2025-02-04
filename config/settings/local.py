from .core import *  # noqa
from decouple import config

DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',  # or 'django.db.backends.postgresql'
        'NAME': os.environ.get('POSTGRES_DB', 'foodanywhere_local'),
        'USER': os.environ.get('POSTGRES_USER', 'postgres'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'postgres'),
        'HOST': os.environ.get('POSTGRES_HOST', 'postgres'),
        'PORT': os.environ.get('POSTGRES_PORT', '5432'),
    }
}


INTERNAL_IPS = ["127.0.0.1"]
DEBUG_TOOLBAR_CONFIG = {"SHOW_TOOLBAR_CALLBACK": lambda _request: DEBUG}
INSTALLED_APPS += ["debug_toolbar"]
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

CELERY_BEAT_SCHEDULE = {
    "auto_expire_transactions": {
        "task": "apps.transactions.tasks.auto_expire_transactions",
        "schedule": timedelta(minutes=20),
    },
}
