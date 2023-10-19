import pytest
from rest_framework.test import APIClient

client = APIClient()


@pytest.mark.django_db
def test_emotion():
    payload = dict(username="santhosh", password="root#1994")
    response = client.post("api/token/", payload)
    assert response.data["username"] == payload["username"]
