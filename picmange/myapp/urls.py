#!/usr/bin/env python
# -*- coding:utf-8 -*-
#__author__=v_zhangjunjie02
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
    #图片信息管理路由
    url(r'^user/(?P<pIndex>[0-9]*)/$', views.user,name='user'),
    #加载添加页面
    url(r'^adduser/$', views.AddUser,name='adduser'),
    #执行添加操作
    url(r'^insertuser/$', views.InsertUser,name='insertuser'),
    #删除信息
    url(r'^user/del/(?P<uid>[0-9]+)$', views.DelUser, name='deluser'),
    #加载修改信息
    url(r'^user/edit/(?P<uid>[0-9]+)$', views.EditUser, name='edituser'),
    #执行修改操作
    url(r'^user/updateuser$', views.UpdateUser, name='updateuser'),







]