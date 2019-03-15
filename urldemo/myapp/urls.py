#!/usr/bin/env python
# -*- coding:utf-8 -*-
#__author__=v_zhangjunjie02
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^fun/2018', views.fun,name='fun'),
    url(r'^fun2/([a-z]{4})', views.fun2,name='fun2'),
    url(r'^fun3/([a-z]{4})/([0-9]+)',views.fun3),
    url(r'^fun4/(?P<yy>[a-z]{4})/(?P<name>[0-9]+)',views.fun4),
    url(r'^fun5/',views.fun5),
    url(r'^fun5/([a-z]+)',views.fun5),

]
