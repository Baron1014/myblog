from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Post
from datetime import datetime
# Create your views here.

def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request, 'index.html', locals())

def showpost(request, slug):
    try:
        post = Post.objects.get(slug=slug)
        if post !=None:
            return render(request, 'post.html', locals())
    except:
        return redirect('/')

def about(request):
    quote = 'Give more than you planned to.'
    return render(request, 'about.html', locals())

def listing(request):
    products = Post.objects.all()
    return render(request, 'list.html', locals())

def disp_detail(request, title):
    try:
        p = Post.objects.get(title=title)
    except Post.DoesNotExist:
        raise Http404('找不到歌曲')

    return render(request, 'disp.html', locals())

def index(request):
    quote = 'Give more than you planned to.'
    return render(request, 'index_ugly.html', locals())