from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase


class WeakData:
    # Authentication
    username = 'usuario'
    password = 'contrasegna'
    # Authentication
    auth_data = {
        'username': username,
        'password': password
    }
    # Product
    product_data = {
        'name': 'Test product',
        'stock': 10,
        'price': 300
    }
    # Payment
    payment_data = {
        'method': 'Débito'
    }
    # Sale
    sale_data = {
        "quantity_sold": 1,
        "product": 1,
        "payment": 1
    }


class TestSetup(APITestCase, WeakData):
    def setUp(self) -> None:
        # Urls
        self.product_url = reverse('products-list')
        self.payment_url = reverse('payments-list')
        self.sale_url = reverse('sales-list')
        self.auth_url = reverse('token_auth')
        # Create a super user in order to authentication works
        User.objects.create_user(
            username='usuario', email='usuario@mail.com', password='contrasegna')
        # First post to get token
        self.auth_response = self.client.post(
            self.auth_url, self.auth_data, format='json')
        self.jwt_token = self.auth_response.data['access']
        # Next post/get's will require the token to connect
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer {0}'.format(self.jwt_token))

        return super().setUp()
