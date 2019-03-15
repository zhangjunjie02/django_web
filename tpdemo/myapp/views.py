from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from myapp.models import District

# Create your views here.
#首页代码
def index(request):
    return render(request,'myapp/index.html')

#加载网页
def showdistrict(request):
    return render(request,'myapp/district.html')

#ajax加载城市信息
def district(request,upid):
    dlist=District.objects.filter(upid=upid)
    list=[]
    for ob in dlist:
        list.append({'id':ob.id,'name':ob.name})
    return JsonResponse({'data':list})
