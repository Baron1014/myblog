from django.contrib import admin
from .models import About, Education, Work
# Register your models here.

class EducationAdmin(admin.ModelAdmin):
    list_display=('degree','school', 'department', 'graduate_year')
    ordering=('-degree', )
 
class WorkAdmin(admin.ModelAdmin):
    list_display=('title', 'department', 'company')

admin.site.register(About)
admin.site.register(Education, EducationAdmin)
admin.site.register(Work, WorkAdmin)