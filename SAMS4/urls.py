"""SAMS4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import xadmin
from django.conf import settings
from django.contrib import admin
from Studentapp import views as v2
from django.views.static import serve
from ApartmentSystem import views as v1
from django.conf.urls.static import static
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', xadmin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('captcha/', include('captcha.urls')),
    path('manager/', include('Managerapp.urls', namespace='manager')),
    path('student/', include('Studentapp.urls', namespace='student')),
    path('index/', v1.index, name='index'),
    path('base/', v1.base, name='base'),
    path('supervisor/',include('Supervisor.urls',namespace='supervisor')),
    re_path(r'news/(?P<content_id>\d+)', v2.News.as_view()),
    path('homelink/', include('homelink.urls')),
]
