# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from . import models

def user_profile(request):
    return render(request, 'profile.html')

def signup(request):
	return render(request, 'login.html')