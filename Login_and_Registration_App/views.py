from django.contrib import messages
from django.shortcuts import render ,redirect
import bcrypt
from .models import *

def index(request):
    return render(request,"index.html")



def register(request):
    if request.method=='POST':
        errors=users.objects.validator(request.POST)
        if len(errors) > 0:
            for key , value in errors.items():
                messages.error(request,value)
            
            return redirect('/')
        else:
            firest_name=request.POST['firest_name']
            last_name=request.POST['last_name']
            email=request.POST['email']
            password=request.POST['password']
            pwhash=bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()
            new_user=users.objects.create(firest_name=firest_name,last_name=last_name,email=email,password=pwhash)
            new_user.save()
            request.session['loggedInUser'] = new_user.id
            return redirect('/sucess')


def login(request):
    if request.method=='POST':
        users_all = users.objects.filter(email=request.POST['email'])
        if len(users_all)==1:
            if not bcrypt.checkpw(request.POST['password'].encode(),users_all[0].password.encode()):
                messages.error(request, "Email or Password is incorrect!")
                return redirect('/')
            else:
                request.session['loggedInUser'] = users_all[0].id
                return redirect('/sucess')
        else:
            messages.error(request, "Email does not exist!")
            return redirect('/')



def sucess(request):
    if not 'loggedInUser'in request.session:
        return redirect('/')
    else:
        context={
        'user':users.objects.get(id=request.session['loggedInUser'])
    }


    
    return render (request,'sucess.html',context)


def logout(request):
    request.session.clear()
    return redirect('/')

