from django.shortcuts import render
import os
from datetime import datetime

def home_page(request):
    return render(request, 'home.html')

def current_time(request):
    now = datetime.now()
    return render(request, 'time.html', {'current_time': now})

def workdir(request):
    path = os.getcwd()
    files = os.listdir(path)
    return render(request, 'workdir.html', {'path': path, 'files': files})