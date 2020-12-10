from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def homepage(request):
    user = request.user
    hello = 'Hello world'

    context = {
        'user': user,
        'hello': hello,
    }
    return render(request, 'connect2/home.html')


def test(request):
    return render(request, 'connect2/test.html')
