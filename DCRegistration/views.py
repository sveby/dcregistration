from django.shortcuts import render
from django.http import *

from django.template import RequestContext, loader

def home(request):
    return HttpResponse("test")
