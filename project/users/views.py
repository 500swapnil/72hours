# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from . import models
from .forms import UserForm, SellerForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from models import User, Item
import datetime


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

def category(request, category_name=None):
    if category_name != 'index' and category_name:
    	category.items = Item.objects.get(category = category_name)
        category.name = category_name

        return render(request, 'category.html', {'items':category.items})

def item(request, item_id):
    Items = Item.objects.all()
    for i in Items:
        if i.id == int(item_id):
	    break
    obj = i
    seller = obj.seller_id
    return render(request, 'item.html', {'item': obj, 'seller': seller})

def contact(request):
    return render(request, 'contact-us.html')

def sell(request):
    return render(request, 'sell.html')
# def login(request):
# 	if request.method == 'POST':
# 		form = UserForm(request.POST)
# 		if form.is_valid():
# 			temp = User.objects.filter(name=form.cleaned_data.get('name'))

def selldone(request):
    if request.method == 'POST':
        form = SellerForm(request.POST, request.FILES)
        temp = User.create("Mridul", "msdvhosd", "saiuga")

        temp.save()
        if form.is_valid():
            temp2 = Item.create(form.cleaned_data.get('name'),datetime.datetime.now,temp,form.cleaned_data.get('description'), form.cleaned_data.get('price'),form.cleaned_data.get('image'),form.cleaned_data.get('quantity'),form.cleaned_data.get('category'))
            temp2.save()
            return render(request, 'home.html')
        else:
            return render(request, 'selldone.html', {'show':form.errors})
