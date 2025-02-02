import os

# All base settings for Django
from .base import *

from .installed import *

ALLOWED_HOSTS = ['*']
DEBUG = False



#SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", 'd-0p71w*5&2xub-i9c7a_#9y=0sr*elu=))033#3l5m_u&ehjz')
print("using production")

# Database
HOME_PAGE_MSG = "Hello World. This is a Local Is a Production"
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'prod.sqlite3',
    }
}