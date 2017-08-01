import os
from django.conf import settings

DEBUG = True
ALLOWED_HOSTS =  ['project-help.herokuapp.com', '.yourdomain.com']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(settings.BASE_DIR, 'db.sqlite3'),
    }
}

# add this
import dj_database_url
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
DATABASES['default']['CONN_MAX_AGE'] = 500

STATIC_ROOT = 'staticfiles'

STATICFILES_DIRS = (
    os.path.join(settings.BASE_DIR, 'static'),
)

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'