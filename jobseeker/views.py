from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'employee/dashboard.html')


def employee(request):
    return render(request, 'employee/employee.html')


def employer(request):
    return render(request, 'employee/employer.html')


def login(request):
    return render(request, 'employee/login.html')
