# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class User (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    address = models.CharField(max_length=255, default=None, null=True)
    number = models.IntegerField(default=None, null=True)

    @classmethod
    def create(cls, name, email, password, address=None, number=None):
        user = cls(name=name, number=number, email=email, address=address, password=password)
        return user

class Item (models.Model):

    CHOICES= (
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
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    date = models.DateField(auto_now=True)
    seller_id = models.ForeignKey(User)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='./users/static/')
    quantity = models.IntegerField()
    category = models.CharField(max_length=40,
        choices=CHOICES
        )

    @classmethod
    def create(cls, title, date, seller_id, description, price, image, quantity, category):
        item = cls(title=title, date=date, seller_id=seller_id, description=description, price=price, image=image, quantity=quantity, category=category)
        return item
        
class Transaction (models.Model) :
    PAYMENT_MODES = (
        ('COD', 'Cash on delivery'),
        ('Online', 'Online')
    )

    id = models.AutoField(primary_key=True)
    seller = models.ForeignKey(User)
    # buyer = models.ForeignKey(User)
    item = models.ForeignKey(Item)
    amount = models.IntegerField()
    payment_mode = models.CharField(max_length=15, choices = PAYMENT_MODES)
    quantity = models.IntegerField()
    time = models.DateTimeField()
