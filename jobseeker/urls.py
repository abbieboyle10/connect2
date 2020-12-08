from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('employee/', views.employee),
    path('employer/', views.employer),
    path('login/', views.login),

]
