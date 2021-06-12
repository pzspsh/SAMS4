# !/usr/bin/python
# -*- coding:utf-8 -*-
# Author:Pan
# @Time:2020/5/20 12:16
# Project_name: SAMS4
# Name: forms

from django import forms
from captcha.fields import CaptchaField


class SupervisorForm(forms.Form):
    sgy_no = forms.CharField(label='宿管员号', max_length=128, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'ID', 'autofocus': ''}))
    password = forms.CharField(label='密码', max_length=256,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    captcha = CaptchaField(label='验证码')
