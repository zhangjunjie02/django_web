#!/usr/bin/env python
# -*- coding:utf-8 -*-
#__author__=v_zhangjunjie02
from django.conf.urls import url
from . import views

urlpatterns = [
    #当前应用的主入口视图
    url(r'^$', views.index,name='index'),
    #httpResponse 实例路由
    url(r'^rp/(?P<cn>[a-z])$', views.rpdemo,name='rpdemo'),
    #httpRequest  实例路由
    url(r'^rq$', views.rqdemo,name='rqdemo'),
    #验证码路由
    url(r'^veritycode$', views.verifycode,name='veritycode'),


]