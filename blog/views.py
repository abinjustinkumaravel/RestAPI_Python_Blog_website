from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse


def index(request):
    return render(request,'templates/index.html')

def detail(request,user_id):
    return render(request,'templates/details.html')

def new_url(request):
    return HttpResponse("<h1>Redirct sucessfull<h1>")

def old_url(request):
    return redirect(reverse('blog:new_url'))
