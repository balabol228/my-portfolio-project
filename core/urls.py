from django.urls import path
from core.views import IndexView, InstructorListView, StudentListView, CarListView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('instructors/', InstructorListView.as_view(), name='instructor_list'),
    path('students/', StudentListView.as_view(), name='student_list'),
    path('cars/', CarListView.as_view(), name='car_list'),
]
