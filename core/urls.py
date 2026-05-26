from django.urls import path
from .views import index, car_list, instructor_list, student_list


urlpatterns = [
    path('', index, name='index'),
    path('cars/', car_list, name='car-list'),
    path('instructors/', instructor_list, name='instructor-list'),
    path('students/', student_list, name='student-list'),
]
