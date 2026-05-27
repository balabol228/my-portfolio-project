from django.test import TestCase
from django.urls import reverse
from core.models import Car, Instructor, Student


class DrivingSchoolModelTests(TestCase):
    def setUp(self):
        self.car = Car.objects.create(
            brand="Toyota", model="Camry", license_plate="BC1111AA"
        )
        self.instructor = Instructor.objects.create(
            first_name="Іван", last_name="Петренко"
        )
        self.student = Student.objects.create(first_name="Олег", last_name="Сидоров")

    def test_car_creation(self):
        self.assertEqual(self.car.brand, "Toyota")
        self.assertEqual(self.car.model, "Camry")

    def test_car_string_representation(self):
        self.assertIn("Toyota", str(self.car))

    def test_instructor_creation(self):
        self.assertEqual(self.instructor.first_name, "Іван")
        self.assertEqual(self.instructor.last_name, "Петренко")

    def test_instructor_string_representation(self):
        self.assertIn("Іван", str(self.instructor))

    def test_student_creation(self):
        self.assertEqual(self.student.first_name, "Олег")
        self.assertEqual(self.student.last_name, "Сидоров")


class DrivingSchoolViewTests(TestCase):
    def setUp(self):
        self.car = Car.objects.create(
            brand="Ford", model="Focus", license_plate="BC2222BB"
        )
        self.instructor = Instructor.objects.create(
            first_name="Марія", last_name="Іванова"
        )
        self.student = Student.objects.create(first_name="Денис", last_name="Балюк")

    def test_index_view_status_code(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_index_view_template(self):
        response = self.client.get(reverse("index"))
        self.assertTemplateUsed(response, "core/index.html")

    def test_index_view_context_data(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.context["num_cars"], 1)
        self.assertEqual(response.context["num_instructors"], 1)
        self.assertEqual(response.context["num_students"], 1)

    def test_instructor_list_view_status(self):
        response = self.client.get(reverse("instructor_list"))
        self.assertEqual(response.status_code, 200)

    def test_instructor_list_context(self):
        response = self.client.get(reverse("instructor_list"))
        self.assertTrue("instructors" in response.context)

    def test_student_list_view_status(self):
        response = self.client.get(reverse("student_list"))
        self.assertEqual(response.status_code, 200)

    def test_student_list_context(self):
        response = self.client.get(reverse("student_list"))
        self.assertTrue("students" in response.context)

    def test_car_list_view_status(self):
        response = self.client.get(reverse("car_list"))
        self.assertEqual(response.status_code, 200)

    def test_car_list_context(self):
        response = self.client.get(reverse("car_list"))
        self.assertTrue("cars" in response.context)
