import os
BASE_DIR= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MYSQL = {
    'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'buensabor',
            'USER': 'root',
            'PASSWORD': 'teuuslib1',
            'HOST': 'localhost',
            'PORT': '3306',
        }
}

SQLITE = {
    'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR,'db/sqlite/sqlite3'),
        }
}