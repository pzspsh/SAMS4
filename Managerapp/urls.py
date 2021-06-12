# !/usr/bin/python
# -*- coding:utf-8 -*-
# Author:Pan
# @Time:2020/5/10 17:47
# Project_name: SAMS4
# Name: urls

from django.urls import path, include,re_path
from Managerapp import views

app_name = 'Manager'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('addStudent/', views.addStudent, name='addStudent'),
    path('addApartment/',views.addApartment,name='addApartment'),
    path('addFloor/',views.addFloor,name='addFloor'),
    path('addIllegal/',views.addIllegal,name='addIllegal'),
    path('addLx/',views.addLx,name='addLx'),
    path('addManager/',views.addManager,name='addManager'),
    path('addSdb/',views.addSdb,name='addSdb'),
    path('addSgy/',views.addSgy,name='addSgy'),
    path('addSsws/',views.addSsws,name='addSsws'),
    path('addSthfix/',views.addSthfix,name='addSthfix'),
    path('select/', views.select, name='select'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('home/',views.content_list,name='home'),
    re_path(r'^echo/(?P<userid>[0-9]+)$',views.echo,name='echo')
]
