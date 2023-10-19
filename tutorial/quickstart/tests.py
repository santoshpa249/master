# from django.test import TestCase
from django.urls import reverse, include, path
from rest_framework.test import APITestCase
from rest_framework import status

# Create your tests here.


class GetEmotions(APITestCase):
    # urlpatterns = [
    #     path("quickstart/", include('quickstart.urls'))
    # ]

    def test_getemotions(self):
        url = reverse("emotions_data")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
