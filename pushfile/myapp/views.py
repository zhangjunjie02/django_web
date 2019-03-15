from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
import time,os
from myapp.models import User
from django.core.paginator import Paginator

# Create your views here.
#首页
def index(request):
    return render(request,'myapp/index.html')
#文件上传
def demo1(request):
    return render(request,'myapp/demo1.html')
@csrf_exempt
def upload(request):
    myfile=request.FILES.get("mypic",None)
    print(myfile)
    if not myfile:
        return HttpResponse("没有上传文件信息")
    filename=str(time.time())+"."+myfile.name.split('.').pop()
    destination=open("./static/pics/"+filename,"wb+")
    for chunk in myfile.chunks():
        destination.write(chunk)
    destination.close()

    #执行图片缩放
    im=Image.open("./static/pics/"+filename)
    #缩放到75*75（缩放后的宽高比例不变）
    im.thumbnail((192,120))
    #把缩放后的图片用jpeg格式保存
    im.save("./static/pics/s_"+filename,None)
    return HttpResponse("ok")

def demo2(request,pIndex):
    list=User.objects.all()
    p=Paginator(list,4)
    if pIndex == "":
        pIndex ="1"
    list2 = p.page(pIndex)
    plist=p.page_range
    context={"ulist":list2,"plist":plist,"pIndex":int(pIndex)}
    return render(request,'myapp/demo2.html',context)
def demo3(request):
    return render(request,'myapp/demo3.html')

#静态文件
def demo4(request):
    return render(request,'myapp/demo4.html')
def demo5(request):
    #session设置
    # request.session['name']='张三'
    #session获取
    name=request.session.get('name',default=None)
    print(name)
    return HttpResponse("状态保持页")





