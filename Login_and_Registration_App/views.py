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
            Fname=request.POST['Fname']
            Lname=request.POST['Lname']
            Email=request.POST['Email']
            Password=request.POST['Password']
            pwhash=bcrypt.hashpw(Password.encode(),bcrypt.gensalt()).decode()

            new_user=users.objects.create(Fname=Fname,Lname=Lname,Email=Email,Password=pwhash)
            new_user.save()
            request.session['loggedInUser'] = new_user.id
            return redirect('/sucess')

            
        

    




def login(request):
    if request.method=='POST':
        users_all = users.objects.filter(Email=request.POST['Email'])
        if len(users_all)==1:
            if not bcrypt.checkpw(request.POST['Password'].encode(),users_all[0].Password.encode()):
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

