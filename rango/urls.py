# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 13:24:00 2019

@author: austin.schrader
"""

from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about')
]