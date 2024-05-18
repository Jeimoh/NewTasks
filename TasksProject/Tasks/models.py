from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length = 40)
    description = models.TextField(null = True, blank = True)
    date_created = models.DateTimeField(auto_now_add = True)
    date_due = models.DateTimeField()
    user = models.ForeignKey(User, on_delete = models.CASCADE,null = True)

    def __str__(self):
        return self.title
    
class Collaboration(models.Model):
    participants = models.ManyToManyField(User,related_name='participates_tasks')
    creator = models.ForeignKey(User, on_delete = models.SET_NULL,null = True, related_name='created_tasks')
    task = models.ForeignKey(Task, on_delete = models.CASCADE,null = True,)
    date_created = models.DateTimeField(auto_now_add = True)
    date_due = models.DateTimeField()

    def __str__(self):
        return self.task
    
     
    