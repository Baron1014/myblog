from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Post
from datetime import datetime
# Create your views here.

def index(request):
    quote = 'Give more than you planned to.'
    return render(request, 'index.html', locals())