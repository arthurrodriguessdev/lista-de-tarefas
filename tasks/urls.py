from django.urls import path
from tasks.views import helloWorld

urlpatterns = [
    path('hello', helloWorld, name='hello')
]