from django.shortcuts import render
from .models import Car, Instructor, Student


def car_list(request):
    cars = Car.objects.all()
    return render(request, 'core/car_list.html', {'cars': cars})


def instructor_list(request):
    instructors = Instructor.objects.all()
    return render(request, 'core/instructor_list.html', {'instructors': instructors})


def student_list(request):
    students = Student.objects.all()
    return render(request, 'core/student_list.html', {'students': students})
