# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from . import models
from .forms import UserForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from models import User, Item

def user_profile(request):
    return render(request, 'profile.html')

def signup(request):
    form = UserForm()
    return render(request, 'login.html', {'form': form})

def thanks(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            temp = User.create(form.cleaned_data.get('name'), form.cleaned_data.get('email'), form.cleaned_data.get('password'))
            temp.save()
        items = Item.objects.all()[0:6]
    return render(request, 'index.html', {'items': items})

def category(request):
	return render(request, 'category.html')

def contact(request):
	return render(request, 'contact-us.html')
# def login(request):
# 	if request.method == 'POST':
# 		form = UserForm(request.POST)
# 		if form.is_valid():
# 			temp = User.objects.filter(name=form.cleaned_data.get('name'))
