from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
now = datetime.datetime.now()
date_now = now.date()


tasks = [
    {'id': 1, 'name': 'Wake up', 'Date': date_now},
    {'id': 2, 'name': 'Take a strong Breakfast', 'Date': date_now},
    {'id': 3, 'name': 'Go for a morning Run', 'Date': date_now},
    {'id': 4, 'name': 'Code', 'Date': date_now},
]
def home(request):
    context = {'tasks': tasks}
    return render(request, 'Tasks/index.html',context)

def task(request,pk):
    task = None
    for i in tasks:
        if i['id'] == int(pk):
            task = i
    context = {'task': task}
    return render(request, 'Tasks/task.html',context)
