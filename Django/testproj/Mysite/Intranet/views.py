from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def login_user(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect('home_page')
        else:
            messages.success(request,("Your credential is invalid!"))
            return redirect('login_user')
    else:
        return render(request,'authenticate/login.html')

@login_required    
def home_page(request):
    return HttpResponse("Hello, you are at homepage")