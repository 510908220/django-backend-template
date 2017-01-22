import os
DEBUG = True
# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#DATABASES
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        "HOST": "db",
        'USER': 'root',
        "PASSWORD": os.environ['DB_PASSWORD'],
        'NAME': os.environ['DB_NAME'],
        'TEST': {'CHARSET': 'UTF8'}
    }
}

