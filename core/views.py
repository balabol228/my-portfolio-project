from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from core.models import Car, Instructor, Student


class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')


class IndexView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_cars'] = Car.objects.count()
        context['num_instructors'] = Instructor.objects.count()
        context['num_students'] = Student.objects.count()
        return context


class CarListView(ListView):
    model = Car
    template_name = 'core/car_list.html'
    context_object_name = 'cars'


class CarCreateView(LoginRequiredMixin, CreateView):
    model = Car
    fields = '__all__'
    template_name = 'core/car_form.html'
    success_url = reverse_lazy('car_list')


class CarUpdateView(LoginRequiredMixin, UpdateView):
    model = Car
    fields = '__all__'
    template_name = 'core/car_form.html'
    success_url = reverse_lazy('car_list')


class CarDeleteView(LoginRequiredMixin, DeleteView):
    model = Car
    template_name = 'core/car_confirm_delete.html'
    success_url = reverse_lazy('car_list')


class InstructorListView(ListView):
    model = Instructor
    template_name = 'core/instructor_list.html'
    context_object_name = 'instructors'


class InstructorCreateView(LoginRequiredMixin, CreateView):
    model = Instructor
    fields = '__all__'
    template_name = 'core/instructor_form.html'
    success_url = reverse_lazy('instructor_list')


class InstructorUpdateView(LoginRequiredMixin, UpdateView):
    model = Instructor
    fields = '__all__'
    template_name = 'core/instructor_form.html'
    success_url = reverse_lazy('instructor_list')


class InstructorDeleteView(LoginRequiredMixin, DeleteView):
    model = Instructor
    template_name = 'core/instructor_confirm_delete.html'
    success_url = reverse_lazy('instructor_list')


class StudentListView(ListView):
    model = Student
    template_name = 'core/student_list.html'
    context_object_name = 'students'


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    fields = '__all__'
    template_name = 'core/student_form.html'
    success_url = reverse_lazy('student_list')


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    fields = '__all__'
    template_name = 'core/student_form.html'
    success_url = reverse_lazy('student_list')


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = 'core/student_confirm_delete.html'
    success_url = reverse_lazy('student_list')
