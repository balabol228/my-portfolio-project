from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('cars/', views.CarListView.as_view(), name='car_list'),
    path('cars/create/', views.CarCreateView.as_view(), name='car_create'),
    path('cars/<int:pk>/update/', views.CarUpdateView.as_view(), name='car_update'),
    path('cars/<int:pk>/delete/', views.CarDeleteView.as_view(), name='car_delete'),
    path('instructors/', views.InstructorListView.as_view(), name='instructor_list'),
    path('instructors/create/', views.InstructorCreateView.as_view(), name='instructor_create'),
    path('instructors/<int:pk>/update/', views.InstructorUpdateView.as_view(), name='instructor_update'),
    path('instructors/<int:pk>/delete/', views.InstructorDeleteView.as_view(), name='instructor_delete'),
    path('students/', views.StudentListView.as_view(), name='student_list'),
    path('students/create/', views.StudentCreateView.as_view(), name='student_create'),
    path('students/<int:pk>/update/', views.StudentUpdateView.as_view(), name='student_update'),
    path('students/<int:pk>/delete/', views.StudentDeleteView.as_view(), name='student_delete'),
]
