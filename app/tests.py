from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.


class Convtemptest(SimpleTestCase):

    def setUp(self):
        self.url = reverse('temp')
        
    def test_ConvTemp_response(self):

        post_dict = {'Value':50, 'Units':'fahrenheit'}

        response = self.client.post(self.url, post_dict)

        self.assertEqual(response.status_code, 201)

    
        self.assertEqual(response.json().get('answer'), "10.0008 celsuis")

    def test_ConvTemp_no_unit_response(self):

        post_dict = {'Value':50, 'Units':''}

        response = self.client.post(self.url, post_dict)

        self.assertEqual(response.status_code, 201)

    
        self.assertEqual(response.json().get('answer'), " ENTER VALUE OR UNIT")

    def test_ConvTemp_no_value_response(self):

        post_dict = {'Value':'', 'Units':'fahrenheit'}

        response = self.client.post(self.url, post_dict)

        self.assertEqual(response.status_code, 201)


        self.assertEqual(response.json().get('answer'), " ENTER VALUE OR UNIT")

    def test_ConvTemp_no_unit_no_value_response(self):

        post_dict = {'Value':'', 'Units':''}

        response = self.client.post(self.url, post_dict)

        self.assertEqual(response.status_code, 201)


        self.assertEqual(response.json().get('answer'), " ENTER VALUE OR UNIT")





