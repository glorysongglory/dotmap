#coding=utf-8
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponse, JsonResponse
from .models import Pageview
import json


# Create your views here.
def mainboard(request):
    return render(request, 'dotmap/index.html', {})
    
    
def api(request, datenumber=None):

    if datenumber and len(datenumber) == 8:
        rows = Pageview.objects.filter(dtime=datenumber).all()
        dlist = []

        for row in rows:
            tmpdict = {}
            tmpdict['name'] = row.city
            tmpdict['value'] = row.count
            dlist.append(tmpdict)
        
        
        data = json.dumps(dlist,skipkeys=False,ensure_ascii=False)
        response = HttpResponse(data)
        response['Content-Type'] = "application/json"
        response['Access-Control-Allow-Origin'] = "*"
        
        return response
    else:
        raise Http404("接口调用错误！")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        