# !/usr/bin/python
# -*- coding:utf-8 -*-
# Author:Pan
# @Time:2020/5/10 17:47
# Project_name: SAMS4
# Name: forms
from django import forms
from captcha.fields import CaptchaField
from ApartmentSystem.models import Comment, TbStudent


class StudentForm(forms.Form):
    stuid = forms.CharField(label='账号', max_length=128, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'ID', 'autofocus': ''}))
    password = forms.CharField(label='密码', max_length=256,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    captcha = CaptchaField(label='验证码')


class RegisterForm(forms.Form):
    gender = (
        ('0', '女'),
        ('1', '男'),
    )
    stuname = forms.CharField(label='用户名', max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    stuid = forms.CharField(label='账号', max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='密码', max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='确认密码', max_length=256,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='邮箱地址', widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label='电话', widget=forms.TextInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label='性别', choices=gender)
    captcha = CaptchaField(label='验证码')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class UserForm(forms.ModelForm):
    class Meta:
        model = TbStudent
        fields = ['s_no']
