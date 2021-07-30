from django.shortcuts import render,redirect
from . models import blog
from . forms import blog_form
from django.http.response import HttpResponseRedirect
from django.http import HttpResponse
from .forms import signup_form
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm,SetPasswordForm,AuthenticationForm
from django.conf import settings


# Create your views here.

def Home(request):
    return render(request,"home.html")


def signup(request):
    if request.method=="POST":
        form = signup_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login/')
    else:
        form=signup_form()
    return render(request,'signup.html',{'form':form})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            form = AuthenticationForm(request,data=request.POST)
            if form.is_valid():

                uname=form.cleaned_data['username']
                upass=form.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/profile/')
        else:
            form=AuthenticationForm()
        return render(request,'userlogin.html',{'form':form})
    else:
        return HttpResponseRedirect('/profile/')


def user_logout(request):
    logout(request)
    return redirect(Home)


def pass1(request):
    if request.method=="POST":
        form=PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return HttpResponseRedirect('/login/')
    else:
        form=PasswordChangeForm(request.user)
    return render(request,'password.html',{'form':form})


def pass2(request):
    if request.method=="POST":
        form=SetPasswordForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return HttpResponseRedirect('/profile/')
    else:
        form=SetPasswordForm(request.user)
    return render(request,'password.html',{'form':form})


def profile(request):
    return render(request,'profile.html')    


def Post(request):
    if request.method=="POST":
        form=blog_form(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect(Read)
        
    else:
        form=blog_form()
    return render(request,"post.html",{"form":form})

def Read(request):
    read=blog.objects.all()
    return render(request,"read.html",{"read":read})

def Update(request,id):
    upd= blog.objects.get(id=id)
    update=blog_form(request.POST or None,request.FILES or None,instance=upd)
    if update.is_valid():
        update.save()
        return redirect(Read)
    return render(request,"update.html",{"update":update})

def Delete(request,id):
    del_t=blog.objects.get(id=id)
    del_t.delete()

    return redirect(Read)
    
    