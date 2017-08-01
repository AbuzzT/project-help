DEBUG = False
ALLOWED_HOSTS =  ['project-help.herokuapp.com', '.yourdomain.com']

# add this
import dj_database_url
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
DATABASES['default']['CONN_MAX_AGE'] = 500