# !/usr/bin/python
# -*- coding:utf-8 -*-
# Author:Pan
# @Time:2020/5/10 17:47
# Project_name: SAMS4
# Name: urls

from django.urls import path, include
from Studentapp import views

app_name = 'student'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('select/', views.select, name='select'),
    path('update/', views.update, name='update'),
]
