import os
import django_heroku

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

TIME_ZONE = 'America/New_York'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')    #from Heroku - for static file collection
#extra locations to search for static files - from Heroku
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),   #changed from staticfiles to static to enable static files on 'base'
)

django_heroku.settings(locals())

import dj_database_url
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)