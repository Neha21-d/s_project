
from django.shortcuts import render, HttpResponse
from .models import Student

def insert_student(request):
    student = Student(name="Neha", age=22, email="neha@gmail.com")
    student.save()
    return HttpResponse("Student record  was added successfully in student!")
def s_list(request):
    students = Student.objects.all()
    return render(request, 's_app/s_list.html', {'students': students})

