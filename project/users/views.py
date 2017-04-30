# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from . import models
from .forms import UserForm, SellerForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from models import User, Item
import datetime
from django.http import HttpResponse


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
    CHOICES= (
    ('0','NULL'),
    ('1','Cars and Bikes'),
    ('2','Home and Decoration'),
    ('3','Mobile and Tablets'),
    ('4','Home appliances'),
    ('5','Fashion'),
    ('6','Books'),
    ('7','Sports and Fitness'),
    ('8','Laptops and PCs'),
    ('9','Toys and Kids Accessories'),
    )

    name = CHOICES[int(category_name)][1]

    if category_name != 'index' and category_name:
    	category.items = Item.objects.filter(category = category_name)
        category.name = category_name

        return render(request, 'category.html', {'items':category.items, 'name':name})

def item(request, item_id):
    Items = Item.objects.get(id = int(item_id))
    seller = Items.seller_id
    return render(request, 'item.html', {'item': Items, 'seller': seller})

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

def index(request):
    items = Item.objects.all()[0:6]
    return render(request, 'index.html', {'items': items})

def search(request):
    if request.method == 'POST':
        name = "Search Results"
        items_all = Item.objects.all()
        search = request.POST.get('search')
        for item in items_all:
            if search in item.title:
                items.append(item)
        if items:
            return render(request, 'category.html', {'items':items, 'name':name, 'error':""})    
        else:
            return render(request, 'category.html', {'items':items, 'name':name, 'error':"No search results"})