from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from datetime import datetime

# Create your views here.
# def homepage(request):
#     posts = Post.objects.all()
#     post_list = list()
#     for count, post in enumerate(posts):
#         post_list.append("No.{}:".format(str(count))+str(post)+"<br>")
#         post_list.append("<small>"+str(post.body.encode('utf-8'))+"</small><br><br>")
#     return HttpResponse(post_list)

def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request, 'index.html',locals())

def showpost(request, slug):
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            return render(request, 'post.html', locals())
    except:
        return redirect('/')