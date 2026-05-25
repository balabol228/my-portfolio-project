from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=64)
    model = models.CharField(max_length=64)
    license_plate = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.license_plate})"


class Instructor(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    car = models.ForeignKey(
        Car, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name="instructors"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Student(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    group_name = models.CharField(max_length=32)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.group_name})"


class Lesson(models.Model):
    date_time = models.DateTimeField()
    student = models.ForeignKey(
        Student, 
        on_delete=models.CASCADE, 
        related_name="lessons"
    )
    instructor = models.ForeignKey(
        Instructor, 
        on_delete=models.CASCADE, 
        related_name="lessons"
    )

    def __str__(self):
        return f"Урок {self.date_time} | Студент: {self.student.last_name} | Інструктор: {self.instructor.last_name}"