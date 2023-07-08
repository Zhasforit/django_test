# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/home/z/zhasfo69/test/master')
sys.path.insert(1, '/home/z/zhasfo69/test/venv_django/lib/python3.10/site-packages/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'master.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()