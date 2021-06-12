from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'index.html')


def base(request):
    return render(request, 'base.html')
