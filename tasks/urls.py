from django.urls import path
from tasks.views import helloWorld, taskList, yourName

urlpatterns = [
    path('hello', helloWorld, name='hello'),
    path('', taskList, name='task-list'),
    path('yourname/<str:name>', yourName, name='your-name')
]