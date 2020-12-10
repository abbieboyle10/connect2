from django.urls import path
from .views import (
    employee,
    employer,
    my_employee
)

app_name = 'jobseeker'

urlpatterns = [


    path('employer/', employer, name='employer'),
    path('employee/', employee, name='employee'),
    path('my_employee/', my_employee, name='my_employee'),


]
