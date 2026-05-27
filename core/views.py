from django.views.generic import TemplateView, ListView
from core.models import Car, Instructor, Student


class IndexView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_cars'] = Car.objects.count()
        context['num_instructors'] = Instructor.objects.count()
        context['num_students'] = Student.objects.count()
        return context


class InstructorListView(ListView):
    model = Instructor
    template_name = 'core/instructor_list.html'
    context_object_name = 'instructors'


class StudentListView(ListView):
    model = Student
    template_name = 'core/student_list.html'
    context_object_name = 'students'


class CarListView(ListView):
    model = Car
    template_name = 'core/car_list.html'
    context_object_name = 'cars'
