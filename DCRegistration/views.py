from django.shortcuts import render
from django.http import *

from django.template import RequestContext, loader

def home(request):
    data = []
    return render(request, 'app_index.html', data)
