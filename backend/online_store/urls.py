# urls.py
# Django 项目的 URL 配置文件，定义 URL 路由。

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('store.urls')),
]

