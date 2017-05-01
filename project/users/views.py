# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from . import models
<<<<<<< HEAD
from .forms import UserForm, SellerForm, LoginForm
=======


from .forms import UserForm, SellerForm
>>>>>>> 9550dc29fbedf0685f97581ef3ebe7a6da27a8bb
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import User, Item
import datetime
from django.http import HttpResponse


def user_profile(request):
    return render(request, 'profile.html')

def signup(request):
    form = UserForm()
    login = LoginForm()
    return render(request, 'login.html', {'form': form, 'login': login})

def thanks(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            temp = User.create(form.cleaned_data.get('name'), form.cleaned_data.get('email'), form.cleaned_data.get('password'), form.cleaned_data.get('address'),form.cleaned_data.get('contact'))
            temp.save()
        items = Item.objects.all()[0:6]
        request.session['name'] = form.cleaned_data.get('name')
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

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():    
            user = form.login(request)
            if user:
                login(request, user)
                return render(request, 'index.html', {'items': items})
        login = UserForm()
        return render(request, 'login.html', {'form': login, 'login': form})

def selldone(request):
    message = "Thank You for posting the ad"
    return render(request, 'thankyou.html', {'message':message})

def signed(request):
    message = "Thank You for signing up"
    return render(request, 'thankyou.html', {'message':message})

def index(request):
    items = Item.objects.all()[0:6]
    return render(request, 'index.html', {'items': items})

def logout(request):
    del request.session['name']
    items = Item.objects.all()[0:6]
    return render(request, 'index.html', {'items': items})

def search(request):
    items = []
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