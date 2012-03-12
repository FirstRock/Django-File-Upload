import os.path as op
from settings import PROJECT_ROOT

DB_PATH = op.join(PROJECT_ROOT, 'db')

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': op.join(DB_PATH, 'data.sqlite'),
    }
}

SECRET_KEY = '9@-a*+c1ms+25b8h83zjkym=qs$mtdq5i!aqszd$buo5*3mky-'
