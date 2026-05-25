from django.test import TestCase
from django.urls import reverse
from .models import Car


class CarModelAndViewsTest(TestCase):

    def setUp(self):
        self.car = Car.objects.create(
            brand="Toyota",
            model="Camry",
            license_plate="AA1122BB"
        )

    def test_car_str_method(self):
        self.assertEqual(
            str(self.car),
            "Toyota Camry (AA1122BB)"
        )

    def test_car_list_view_status_code(self):
        response = self.client.get(reverse('car-list'))
        self.assertEqual(response.status_code, 200)

    def test_car_list_view_uses_correct_template(self):
        response = self.client.get(reverse('car-list'))
        self.assertTemplateUsed(response, 'core/car_list.html')
