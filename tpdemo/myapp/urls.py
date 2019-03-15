#!/usr/bin/env python
# -*- coding:utf-8 -*-
#__author__=v_zhangjunjie02
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^showdistrict$', views.showdistrict,name='showdistrict'),#加载网页
    url(r'^district/([0-9]+)$', views.district,name='district'),#Ajax加载城市信息



]