#!/usr/bin/env python
# -*- coding:utf-8 -*-
#__author__=v_zhangjunjie02
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index,name='index'),
    #文件上传
    url(r'^demo1$', views.demo1,name='demo1'),
    url(r'^upload', views.upload,name='upload'),
    #数据分页
    url(r'^demo2/(?P<pIndex>[0-9]+)$', views.demo2,name='demo2'),
    #富文本编辑页
    url(r'^demo3$', views.demo3, name='demo3'),
    #静态文件
    url(r'^demo4$', views.demo4, name='demo4'),
    #状态保存
    url(r'^demo5$', views.demo5, name='demo5'),


]
