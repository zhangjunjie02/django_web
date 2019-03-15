from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from myapp.models import User
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator

import time,os
from PIL import Image
# Create your views here.
def index(request):
    return render(request,'myapp/index.html')
def user(request,pIndex):
    #获取用户信息
    list=User.objects.all()
    p=Paginator(list,4)
    if pIndex =='':
        pIndex = '1'
    pIndex=int(pIndex)
    list1=p.page(pIndex)
    plist=p.page_range

    #将信息封装到字典中
    context={'userlist':list1,'plist':plist,'pIndex':pIndex}
    return render(request,'myapp/show.html',context)

#加载添加页面方法
def AddUser(request):
    return render(request,'myapp/add.html')

#执行添加操作的方法
@csrf_exempt
def InsertUser(request):
    try:
        user=User()
        user.title=request.POST['title']
        photo=request.FILES.get('mypic',None)

        user.photo=photo.name
        if not photo:
            return HttpResponse("没有上传图片")
        filename = str(photo.name)
        destination = open("./static/myapp/pics/" + filename, "wb+")
        for chunk in photo.chunks():
            destination.write(chunk)
        destination.close()

        # 执行图片缩放
        im = Image.open("./static/myapp/pics/" + filename)
        # 缩放到75*75（缩放后的宽高比例不变）
        im.thumbnail((192, 120))
        # 把缩放后的图片用jpeg格式保存
        im.save("./static/myapp/pics/s_" + filename, None)

        user.createtime=datetime.now()
        user.save()
        context = {"info": "添加成功"}

    except:
        context = {"info": "添加失败"}
    return render(request,'myapp/info.html',context)
#执行删除方法
def DelUser(request,uid):
    try:
        user=User.objects.get(id=uid)
        user.delete()
        context={"info":"数据删除成功"}
    except:
        context={"info":"数据删除成功"}
    return render(request,'myapp/info.html',context)

#加载修改页面信息
def EditUser(request,uid):
    try:
        ob = User.objects.get(id=uid)
        context = {"user": ob}
        return render(request, 'myapp/edit.html', context)
    except:
        context = {"info": "没有找到要修改的信息"}
    return render(request, 'myapp/edit.html', context)

#执行修改操作
@csrf_exempt
def UpdateUser(request):
    try:
        user = User.objects.get(id=request.POST['id'])

        photo = request.FILES.get('mypic', None)
        user.title = request.POST['title']
        user.photo = photo.name
        user.createtime = datetime.now()
        if not photo:
            return HttpResponse("没有上传图片")
        filename = str(photo.name)
        destination = open("./static/myapp/pics/" + filename, "wb+")
        for chunk in photo.chunks():
            destination.write(chunk)
        destination.close()

        # 执行图片缩放
        im = Image.open("./static/myapp/pics/" + filename)
        # 缩放到75*75（缩放后的宽高比例不变）
        im.thumbnail((192, 120))
        # 把缩放后的图片用jpeg格式保存
        im.save("./static/myapp/pics/s_" + filename, None)

        user.save()

        context = {"info": "修改数据成功"}
    except:
        context = {"info": "修改数据失败"}
    return render(request, 'myapp/info.html', context)


















