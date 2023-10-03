from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from django.db import connection


# Create your views here.
def home(request):
    students = Student.objects.all()
    print(students)
    print(connection.queries[-1])
    pierce = students.filter(firstname="pierce")
    print(pierce)
    print(connection.queries[-1])
    pierce2 = Student.objects.filter(firstname="pierce2")
    print(pierce2)
    print(connection.queries[-1])
    return render(request, "index.html")
    # return HttpResponse("Hello, Django!")
