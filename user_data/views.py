from django.shortcuts import render,redirect
from .forms import *
from django import forms
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib import messages

# Create your views here.

def reg_user(request):
    if request.method == "GET":
        return render(request,template_name="regii.html",context={'form':UserCreationForm()})
    elif request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request,"Sigun Up Succesfully...")

        return redirect("user_login")
    
def user_login(request):
    if request.method == "GET":
        return render(request,"login.html",{"form":AuthenticationForm()})
    elif request.method == "POST":
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            print(user)
            if user:
                login(request,user)
                messages.success(request,"Log In Succesfully..")

                return redirect("home")
            
        messages.error(request,"Invalid Credential")
    
        return redirect("user_login")
    
def log_out(request):
    
    logout(request)
    messages.info(request,"Logout Succesfully")

    return redirect("user_login")

def login_page(request):
    return redirect("user_login")

def user_signup(request):
    return redirect("reg")
