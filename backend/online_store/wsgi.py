# wsgi.py
# WSGI 配置文件，用于部署 Django 项目。

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'online_store.settings')

application = get_wsgi_application()

