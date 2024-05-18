from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime
from .models import Task
from .forms import createTaskForm

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

def createTask(request):
    form = createTaskForm()
    
    if request.method == 'POST':
        form = createTaskForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
    
    context = {'form':form, }
    return render(request, 'Tasks/createTask.html',context)

def updateTask(request, pk):
    task = Task.objects.get(id = pk)
    
    form = createTaskForm(instance=task)
    if request.method == 'POST':
        form = createTaskForm(request.POST, instance = task)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context = {'form':form}
    return render(request, 'Tasks/createTask.html',context)

