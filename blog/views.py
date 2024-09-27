from django.shortcuts import render,redirect
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>wello come to My Blog website<h1>")

def detail(request, user_id):
    return HttpResponse(f"hello your are visiting page of user {user_id} now")

def new_url(request):
    return HttpResponse("<h1>Redirct sucessfull<h1>")

def old_url(request):
    return redirect("new_url")
