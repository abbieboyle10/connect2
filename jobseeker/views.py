from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    user = request.user
    hello = 'Hello world'

    context = {
        'user': user,
        'hello': hello,
    }
    return render(request, 'main/home.html')


def employee(request):
    return render(request, 'employee/employee.html')


def employer(request):
    return render(request, 'employee/employer.html')


def login(request):
    return render(request, 'employee/login.html')
