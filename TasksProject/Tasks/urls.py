from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home, name = "home"),
    path('task/<str:pk>',views.task, name = "task"),

    path('task/t/createTask',views.createTask, name="createTask"),
    path('task/updateTask/<str:pk>',views.updateTask, name = "updateTask"),

    
]