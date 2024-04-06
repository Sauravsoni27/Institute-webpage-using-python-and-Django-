from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.conf import settings
from django.views.decorators.csrf import csrf_protect
import time 
from django.db import connection

curl=settings.CURRENT_URL
def home(request):
    return render(request,"home.html",{'curl':curl})
def about(request):
    return render(request,"about.html",{'curl':curl})
def contact(request):
    return render(request,"contact.html",{'curl':curl})
def service(request):
    return render(request,"service.html",{'curl':curl})
def register(request):
    if request.method=='GET':
        return render(request,"register.html",{'curl':curl,'msg':''})
    else:
        name=request.POST.get("name")
        username=request.POST.get("username")
        password=request.POST.get("password")
        mobile=request.POST.get("mobile")
        address=request.POST.get("address")
        city=request.POST.get("city")
        gender=request.POST.get("gender")
        print(name)
        print(gender)
        info=time.asctime(time.localtime(time.time()))
        #create a query to insert record in database
        sql="insert into register values(NULL,'%s','%s','%s','%s','%s','%s','%s','user',1,'%s')"%(name,username,password,mobile,address,city,gender,info)
        #execute query using cursor instance
        cursor=connection.cursor()
        cursor.execute(sql)

        return render(request,"register.html",{'curl':curl,'msg':'form submitted'})
def login(request):
    if request.method=='GET':
        return render (request,"login.html",{'curl':curl},'msg'"form submitted")
    else:
        username=request.POST.get("username")
        password=request.POST.get("password")
        #query to fetch user details from database
        sql="select *from register where username='%s' and password='%s' and status=1"%(username,password)
        cursor=connection.cursor()
        cursor.execute(sql)
        # return render (request, "login.html",{curl})
        # fetch record from cursor
        userDetails=cursor.fetchone()
        (userDetails)
        if userDetails!=None:

            return render (request,"login.html",{'curl':curl,'msg':'login success'})
        else:
            return render (request,"login.html",{'curl':curl,'msg':'invalid user details'})
    
def adminhome(request):
    return render (request,"adminhome.html",{'curl':curl,})