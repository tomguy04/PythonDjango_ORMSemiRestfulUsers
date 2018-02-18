# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import User
from django.shortcuts import render, HttpResponse, redirect

# the index function is called when root is visited
def index(request):
    # response = "Hello, I am your first request!"
    return render(request,"srusers_app/index.html")

def new(request):
    return render(request,'srusers_app/adduser.html')

def create(request):
    print "*********************IN CREATE"
    u1 = User(first_name = request.POST['first_name'], last_name = request.POST['first_name'], email = request.POST['email'])
    u1.save()
    user_data = u1.id
    user_path = '/users/'+str(user_data)
    print "*********************user_path " + user_path
    return redirect(user_path)
    

def show(request,uid):
    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    print uid
    context = {
        'id':uid,
        'user':User.objects.get(id=uid)
    }

 #   return render_template('user_profile.html',user = user_data[0])
    return render(request,"srusers_app/user_profile.html", context)
    