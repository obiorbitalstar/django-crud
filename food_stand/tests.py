from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Menu
from django.urls import reverse
# Create your tests here.

class SnackTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='Bashar',
            email='bashar@gmail.com',
            password='password'
        )

        self.menu = Menu.objects.create(
            dish_name='shwarma',
            customer =self.user,
            price = 15,
            description='its shwarma no description needed'            
        )

    def test_menu_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_menu_details_view(self):
        response = self.client.get(reverse('dish_details', args='1'))
        self.assertEqual(response.status_code, 200)

    def test_menu_update_view(self):
        response = self.client.post(reverse('update_view', args='1'), {
            'dish_name': 'mansaf',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'mansaf')