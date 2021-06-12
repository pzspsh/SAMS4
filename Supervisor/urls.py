# !/usr/bin/python
# -*- coding:utf-8 -*-
# Author:Pan
# @Time:2020/5/20 11:56
# Project_name: SAMS4
# Name: urls
from django.urls import path, re_path
from Supervisor import views

app_name = 'Supervisor'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/',views.logout,name='logout'),
    path('addillegal/',views.addIllegal,name='addillegal'),
    path('addsdb/',views.addSdb,name='addsdb'),
    path('addssws/',views.addSsws,name='ssws'),
    path('addsthfix/',views.addSthfix,name='addsthfix'),
    path('select/',views.select,name='select'),
    path('delete/',views.delete,name='delete'),
    path('update/',views.update,name='update'),
    path('addlx/',views.addLx,name='lx',)
]
