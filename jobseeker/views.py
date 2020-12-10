from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from .models import *

# Create your views here.


def employer(request=settings.AUTH_USER_MODEL):
    employer = Employer_Basics.objects.get(user=request.user)

    context = {
        'Employer_Basics': employer,
    }

    return render(request, 'employee/employer.html', context)


def my_employee(request):
    return render(request, 'employee/my_employee.html')


def login(request):
    return render(request, 'employee/login.html')


def employee(request=settings.AUTH_USER_MODEL):
    employee = Employee_Basics.objects.get(user=request.user)

    context = {
        'Employee_Basics': employee,
    }

    return render(request, 'employee/employee.html', context)
