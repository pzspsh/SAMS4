# !/usr/bin/python
# -*- coding:utf-8 -*-
# Author:Pan
# @Time:2020/5/22 19:58
# Project_name: SAMS4
# Name: urls

from django.urls import path
from . import views

app_name = 'homelink'

urlpatterns = [
    path('', views.house_index, name='house_index'),
    path('spider/', views.house_spider, name='house_spider'),
]