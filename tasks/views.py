from django.shortcuts import render
from django.http import HttpResponse

def helloWorld(request):
    return HttpResponse("Olá, mundo!")

def taskList(request):
    return render(request, 'list.html')

def yourName(request, name):
    return render(request, 'yourname.html', {'name': name})

