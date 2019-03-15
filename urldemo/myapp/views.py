from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
# Create your views here.
def index(request):
    return HttpResponse("Hello Django!")
def fun(request):
    #return HttpResponse("fun()......")
    return redirect(reverse('index'))
def fun2(request,num):
    return HttpResponse("fun().....%s"%(num))
def fun3(request,num,name):
    return HttpResponse("fun().....%s  %s"%(num,name))
def fun4(request,yy,name):
    return HttpResponse("fun().....%s  %s"%(yy,name))
def fun5(request,num=""):
    return HttpResponse("fun().....%s"%num)
def fun6(request,num=""):
    return HttpResponse("fun().....%s"%num)

