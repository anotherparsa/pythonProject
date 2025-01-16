from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def index(request):
    return HttpResponse("Hello World")

def dynamicdata(request, test):
    return HttpResponse(f'This is {test}')

def redirecting(request):
    return HttpResponseRedirect(reverse('thisishome'))
