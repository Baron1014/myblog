from datetime import datetime, date
from enum import unique
from django.db import models
from django.utils import timezone
from django.core.management import call_command
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class About(models.Model):
    p_name =models.CharField(max_length=10)
    text = models.TextField()

    def __str__(self):
        return self.p_name
    
    class Meta:
        ordering=['p_name']
   
class Education(models.Model):
    DEGREES = (
        ('Bachelor', 'bachelor'),
        ('Master', 'master'),
        ('Exchange Student', 'exchange'),
    )
    school = models.CharField(max_length=30)
    degree = models.CharField(max_length=30, choices=DEGREES)
    start_year = models.IntegerField(default=2015)
    start_month = models.CharField(max_length=10, default="09")
    graduate_year = models.IntegerField(blank=True, null=True)
    graduate_month = models.CharField(max_length=10, blank=True, null=True)
    department = models.CharField(max_length=50)
    seq_id = models.IntegerField(unique=True)

    def __str__(self):
        return self.degree
    
    class Meta:
       ordering=['-seq_id']
        

class Work(models.Model):
    title = models.CharField(max_length=30)
    department = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    start_year = models.IntegerField(default=2018)
    start_month = models.CharField(max_length=10)
    end_year = models.IntegerField(blank=True, null=True)
    end_month = models.CharField(max_length=10, blank=True, null=True)
    

class Honor(models.Model):
    accept_year = models.IntegerField(default=2015)
    award_name = models.CharField(max_length=50)

    def __str__(self):
        return self.award_name
    class Meta:
        ordering = ["-accept_year"]
    
class Competition(models.Model):
    award = models.CharField(max_length=50)
    case_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=80)
    accept_day = models.DateField(default=date.today)
    member = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.case_name
    
    class Meta:
        ordering=['-accept_day']

class Publications(models.Model):
    members = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    accept_day = models.DateField(default=date.today)
    MONTH_CHOICES = [
        ('Jan.', 'January'),
        ('Feb.', 'February'),
        ('Mar.', 'March'),
        ('Apr.', 'April'),
        ('May.', 'May'),
        ('Jun.', 'June'),
        ('Jul.', 'July'),
        ('Aug.', 'August'),
        ('Sep.', 'September'),
        ('Oct.', 'October'),
        ('Nov.', 'November'),
        ('Dec.', 'December'),
    ]

    accept_month = models.CharField(max_length=10, choices=MONTH_CHOICES)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    paper_link = models.URLField(max_length=200)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering=['-accept_day']

class Projects(models.Model):
    title = models.CharField(max_length=18)
    abstract = models.TextField(max_length=250)
    start_year = models.IntegerField(default=2015)
    start_month = models.CharField(max_length=10, default="09")
    end_year = models.IntegerField(blank=True, null=True)
    end_month = models.CharField(max_length=10, blank=True, null=True)
    image = models.ImageField(upload_to='static/images/upload', width_field=None, height_field=None, default="static/images/default_image.jpeg")

    def __str__(self):
        return self.title
    
    class Meta:
       ordering=['-start_year']

@receiver(post_save, sender=Projects)
def run_collectstatic(sender, instance, **kwargs):
    call_command('collectstatic', interactive=False)
