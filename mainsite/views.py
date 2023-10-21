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
    competitions = models.Competition.objects.all()
    publications = models.Publications.objects.all()
    projects = models.Projects.objects.all()
    now = datetime.now()
    format_now = now.strftime("%Y.%m")
    return render(request, 'index.html', locals())
