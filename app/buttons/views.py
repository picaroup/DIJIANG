from django.shortcuts import render
from .models import Users
from django.db import models
from django.utils import timezone
#from calendar import timegm
import time
import random
from django.http import HttpResponse

def generatecode(request):
    code = random.randint(0, 1000000)
    codes = Users.objects.values('code')
    while code in codes:
        code = random.randint(100000, 10000000)
    new_user = Users(code = code)
    new_user.save()
    return render(request, 'buttons/code.html', {"code": code})

def verifycode(request):
    user_ = Users.objects.filter(code = request.POST['verifycode'])
    check = 1
    if len(user_) == 0:
        check = 0
    else:
        user = user_[0]
        new_user = Users()
        new_user.code = request.POST['verifycode']
        user.other_user = new_user
        new_user.other_user = user
        user.save()
        new_user.save()
    return render(request, 'buttons/verify.html', {"check": check})

def mainview(request):
    return render(request, 'buttons/main.html')

def tryy(request):
   temp = request.GET["page"]
   if(temp == "try"):
       return render(request, 'buttons/try.html')
   else:
       return render(request, 'buttons/main.html')

def tutorial(request):
   temp = request.GET["page"]
   return render(request, 'buttons/tutorial.html')

def upload(request):
    return render(request, 'buttons/upload.html')
