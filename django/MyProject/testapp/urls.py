from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home,  name='thisishome'),
    path('redirecting', views.redirecting),
    path('<test>', views.dynamicdata),
]