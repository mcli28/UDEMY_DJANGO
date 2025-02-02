import os

# All base settings for Django
from .base import *

from .installed import *

HOME_PAGE_MSG = "Hello World. This is a Local proxy"
print("using local proxy")
# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'proxy.sqlite3',
    }
}