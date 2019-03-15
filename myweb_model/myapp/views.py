from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import User
from datetime import datetime
from django.shortcuts import redirect
from django.core.urlresolvers import reverse



# Create your views here.


#首页
def index(request):
    return render(request,'myapp/index.html')
#浏览信息
def indexUsers(request):
    # return HttpResponse("indexUsers")
    #或许用户信息
    list=User.objects.all()
    context={"userlist":list}#将信息封装到字典中
    return render(request,'myapp/user/index.html',context)
#加载添加表单
def addUsers(request):
    return render(request,'myapp/user/add.html')
#执行信息添加
def insertUser(request):
    #获取并封装用户信息
    try:
        user=User()
        user.name=request.POST['name']
        user.age = request.POST['age']
        user.phone = request.POST['phone']
        user.addtime = datetime.now()
        user.save()
        context={"info":"添加数据成功"}
    except:
        context={"info":"添加数据失败"}
    return render(request,'myapp/user/info.html',context)

#删除信息
def delUsers(request,uid):
    try:
        user=User.objects.get(id=uid)
        user.delete()
        context = {"info": "删除数据成功"}
    except:
        context = {"info": "删除数据失败"}
    return  render(request,'myapp/user/info.html',context)
#加载修改信息
def editUsers(request,uid):
    try:
        ob=User.objects.get(id=uid)
        context = {"user":ob}
        return render(request,'myapp/user/edit.html',context)
    except:
        context = {"info": "没有找到要修改的信息"}
    return  render(request,'myapp/user/info.html',context)

#执行信息修改
def updateUsers(request):
    # 获取并封装用户信息
    try:
        user = User.objects.get(id=request.POST['id'])
        user.name = request.POST['name']
        user.age = request.POST['age']
        user.phone = request.POST['phone']
        user.addtime = datetime.now()
        user.save()
        context = {"info": "修改数据成功"}
    except:
        context = {"info": "修改数据失败"}
    return render(request, 'myapp/user/info.html', context)










