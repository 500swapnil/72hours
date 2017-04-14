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
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    date = models.DateField()
    seller_id = models.ForeignKey(User)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(max_length=255)
    quantity = models.IntegerField()

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
