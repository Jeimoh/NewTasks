from django.contrib import admin

# Register your models here.
from .models import Task, Collaboration

admin.site.register(Task)
admin.site.register(Collaboration)