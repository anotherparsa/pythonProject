from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse



def home(request):
    return render(request, 'testapp/testapp.html')

def dynamicdata(request, test):
    return HttpResponse(f'This is {test}')

def redirecting(request):
    return HttpResponseRedirect(reverse('thisishome'))
