from datetime import datetime
from enum import unique
from django.db import models
from django.utils import timezone
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
    