from app.tests.test_setup import TestSetup


class TestAuthentication(TestSetup):
    def test_create_token(self):
        self.assertTrue('access' in self.auth_response.data)


class TestProductViews(TestSetup):
    def test_get_products(self):
        response = self.client.get(self.product_url)
        self.assertEqual(response.status_code, 200)

    def test_create_products(self):
        response = self.client.post(self.product_url, data=self.product_data)
        self.assertEqual(response.status_code, 201)


class TestPaymentViews(TestSetup):
    def test_get_payments(self):
        response = self.client.get(self.payment_url)
        self.assertEqual(response.status_code, 200)

    def test_create_payments(self):
        response = self.client.post(self.payment_url, data=self.payment_data)
        self.assertEqual(response.status_code, 201)


class TestSaleViews(TestSetup):
    def test_get_sales(self):
        response = self.client.get(self.sale_url)
        self.assertEqual(response.status_code, 200)
