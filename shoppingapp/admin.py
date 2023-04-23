from django.contrib import admin
from .models import *


admin.site.register(Category)


class JobAdmin(admin.ModelAdmin):
    list_display = ('title','is_published','is_closed','timestamp')

admin.site.register(Job,JobAdmin)


