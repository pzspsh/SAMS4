# !/usr/bin/python
# -*- coding:utf-8 -*-
# Author:Pan
# @Time:2020/5/10 17:46
# Project_name: SAMS4
# Name: forms
from django import forms
from captcha.fields import CaptchaField
from ApartmentSystem.models import *
import re


def email_check(email):
    pattern = re.compile(r"^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$")
    return re.match(pattern, email)


def phone_check(phone):
    pattern = re.compile(r"(13|15|18|17)[0-9]{9}")
    return re.match(pattern, phone)


class ManageForm(forms.Form):
    mid = forms.CharField(label='账号', max_length=128, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'ID', 'autofocus': ''}))
    password = forms.CharField(label='密码', max_length=256,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    captcha = CaptchaField(label='验证码')


class RegisterForm(forms.Form):
    gender = (
        ('0', '女'),
        ('1', '男'),
    )
    mname = forms.CharField(label='用户名', max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    mid = forms.CharField(label='账号', max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='密码', max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='确认密码', max_length=256,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='邮箱地址', widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label='电话', widget=forms.TextInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label='性别', choices=gender)
    captcha = CaptchaField(label='验证码')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email_check(email):
            filter_result = ManageModel.objects.filter(email=email)
            if len(filter_result) > 0:
                raise forms.ValidationError('你的邮箱已存在')
        else:
            raise forms.ValidationError('请你输入一个有效的邮箱')
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone_check(phone):
            filter_result = ManageModel.objects.filter(phone=phone)
            if len(filter_result) > 0:
                raise forms.ValidationError('你的电话已存在！')
        else:
            raise forms.ValidationError('请你输入一个有效的电话！')
        return phone

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 6:
            raise forms.ValidationError('你的密码太短！')
        elif len(password1) > 20:
            raise forms.ValidationError('你的密码太长！')
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('密码匹配不对，请重新输入！')
        return password2
