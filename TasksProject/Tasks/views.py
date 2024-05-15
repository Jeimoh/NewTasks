from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import Task

# Create your views here.
now = datetime.datetime.now()
date_now = now.date()


tasks = Task.objects.all()
def home(request):
    context = {'tasks': tasks}
    return render(request, 'Tasks/index.html',context)

def task(request,pk):
    task = Task.objects.get(id = pk)
    context = {'task': task}
    return render(request, 'Tasks/task.html',context)
