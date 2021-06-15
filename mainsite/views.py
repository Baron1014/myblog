from django.shortcuts import render
from django.http import HttpResponse, Http404
from datetime import datetime
from django.views.decorators.cache import never_cache
from mainsite import models
# Create your views here.

@never_cache
def index(request):
    abouts = models.About.objects.all()
    educations = models.Education.objects.all()
    works = models.Work.objects.all()
    honors = models.Honor.objects.all()
    return render(request, 'index.html', locals())