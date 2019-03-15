#!/usr/bin/env python
# -*- coding:utf-8 -*-
#__author__=v_zhangjunjie02
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^demo1$',views.demo1,name='demo1'),
    url(r'^demo2$', views.demo2, name='demo2'),


]