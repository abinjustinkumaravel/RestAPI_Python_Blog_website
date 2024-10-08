from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
import logging
from .models import Post





# posts =[
#     {'id':1, 'title':'Post 1', 'content':'Content of post 1'},
#     {'id':2, 'title':'Post 2', 'content':'Content of post 2'},
#     {'id':3, 'title':'Post 3', 'content':'Content of post 3'},
#     {'id':4, 'title':'Post 4', 'content':'Content of post 4'},
#     {'id':5, 'title':'Post 5', 'content':'Content of post 5'},
# ]






def index(request):
    blog_title = "Latest Posts"
    posts=Post.objects.all()
    return render(request,'templates/index.html', {'blog_title': blog_title, 'posts':posts})

def detail(request,post_id):

    post=Post.objects.get(pk=post_id)
    # post=next((item for item in posts if item['id']== int(post_id)), None)
    # logger=logging.getLogger("Testing")
    # logger.debug(f"post variable is {post}")
    return render(request,'templates/details.html',{"post":post})


def new_url(request):
    return HttpResponse("<h1>Redirct sucessfull<h1>")

def old_url(request):
    return redirect(reverse('blog:new_url'))