# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render,render_to_response
from django.core import serializers
from models import students
from django.views.decorators.csrf import csrf_exempt,csrf_protect
import json
import sqlite3
import re
# Create your views here.

def init(request):
    #return render(request,"init.html")
    return render_to_response("init.html")

def add(request):
    #return render(request,"init.html")
    return render(request,"add.html")

def addsuccess(request):
    if request.method=='POST':
        students.objects.create(stuid=request.POST['stuid'],name=request.POST['name'],chinese=int(request.POST['chinese']),math=int(request.POST['math']),english=int(request.POST['english']),physics=int(request.POST['physics']),chemistry=int(request.POST['chemistry']),scoresum=(int(request.POST['chinese'])+int(request.POST['math'])+int(request.POST['english'])+int(request.POST['physics'])+int(request.POST['chemistry'])))
        return HttpResponse("添加成功")
        
def score(request):
    #return render(request,"init.html")
    return render(request,"score.html")

@csrf_exempt
def showresult(request):
    if request.method=='POST':
        ret={'status':True,'data':None}
        if request.POST['method']=="search":
            searchinfo=request.POST['searchinfo']
            if re.match(r"^[0-9]+$",searchinfo)!=None:
                try:    
                    student=students.objects.filter(stuid__contains=searchinfo).order_by("-scoresum")
                    ret['data']=serializers.serialize('json',student)
                except Exception:
                    ret['status']=False
                return HttpResponse(json.dumps(ret))
            else:
                try:    
                    student=students.objects.filter(name__contains=searchinfo).order_by("-scoresum")
                    ret['data']=serializers.serialize('json',student)
                except Exception:
                    ret['status']=False
                return HttpResponse(json.dumps(ret))
        else:
            try:
                student=students.objects.all().order_by("-scoresum")
                ret['data']=serializers.serialize('json',student)
            except Exception:
                ret['status']=False
            return HttpResponse(json.dumps(ret))


def change(request):
    if request.method=='POST':
        students.objects.filter(id=int(request.POST['pkre'])).update(name=request.POST['namere'],stuid=request.POST['stuidre'],chinese=int(request.POST['chinesere']),chemistry=int(request.POST['chemistryre']),physics=int(request.POST['physicsre']),math=int(request.POST['mathre']),english=int(request.POST['englishre']),scoresum=int(request.POST['chinesere'])+int(request.POST['chemistryre'])+int(request.POST['physicsre'])+int(request.POST['mathre'])+int(request.POST['englishre']))
        return HttpResponse("修改成功")
def delete(request):
    if request.method=='POST':
        students.objects.get(id=request.POST['pkre']).delete()
        return HttpResponse("删除成功")