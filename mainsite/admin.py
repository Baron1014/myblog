from django.contrib import admin
from . import models
# Register your models here.

class EducationAdmin(admin.ModelAdmin):
    list_display=('degree','school', 'department', 'graduate_year')
    ordering=('-degree', )
 
class WorkAdmin(admin.ModelAdmin):
    list_display=('title', 'department', 'company')


admin.site.register(models.About)
admin.site.register(models.Education, EducationAdmin)
admin.site.register(models.Work, WorkAdmin)
admin.site.register(models.Honor)
admin.site.register(models.Competition)