#!/usr/bin/env python
# -*- coding:utf-8 -*-
#__author__=v_zhangjunjie02
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.index),
    url(r'^stu$',views.stu),
]
