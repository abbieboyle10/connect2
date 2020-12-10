from django.urls import path
from . import views

urlpatterns = [


    path('home', views.homepage),

    path('test/', views.test),



]
