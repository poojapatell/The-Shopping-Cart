
from django.forms import forms
from django.shortcuts import render, HttpResponseRedirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import Form, profileform
# Create your views here.
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm, UserChangeForm
from django.contrib.auth import authenticate,login,logout, update_session_auth_hash

def signup(request):
    if request.method=="POST":
        fm=Form(request.POST)
        if fm.is_valid():
            messages.success(request,'acc bann gya')
            fm.save()
    else:
        fm=Form()
    return render(request,'form.html',{'form':fm})

# login view
def user_login(request):
 if not request.user.is_authenticated:
    if request.method=='POST':
        fm=AuthenticationForm(request.POST, data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            pwd=fm.cleaned_data['password']
            user= authenticate(username=uname,password=pwd)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/enroll/profile/')
    else:
        fm=AuthenticationForm()
    return render(request,'login.html',{'form':fm})
 else:
    return HttpResponseRedirect('/enroll/profile/')
def home(request):
    return render(request,'home.html')
def profile(request):
    if request.user.is_authenticated:
        if request.method=='POST':
         fm=profileform(request.POST,instance=request.user)
         if fm.is_valid():
             fm.save()
             messages.success(request,"profile updated!!")
        else:
         fm=profileform(instance=request.user)
        return render(request,'profile.html',{'name':request.user,'form':fm})
    else:
     return HttpResponseRedirect('/enroll/login/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/enroll/ul/')

def user_cpwd(request):
  if request.user.is_authenticated:
    if request.method=='POST':
        fm= profileform(user=request.user,data=request.POST)
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request,fm.user)
            return HttpResponseRedirect('/enroll/profile/')
    else:
        fm= PasswordChangeForm(user=request.user)
    return render(request,'pwd.html',{'form':fm})
  else:
    return HttpResponseRedirect('/enroll/login/')

def user_cpwd1(request):
  if request.user.is_authenticated:
    if request.method=='POST':
        fm= SetPasswordForm(user=request.user,data=request.POST)
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request,fm.user)
            return HttpResponseRedirect('/enroll/profile/')
    else:
        fm= SetPasswordForm(user=request.user)
    return render(request,'pwd1.html',{'form':fm})
  else:
    return HttpResponseRedirect('/enroll/login/')
