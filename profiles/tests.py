from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Profiles
import pytest

# Create your tests here.


@pytest.mark.django_db
def test_index_url(client):
    path = reverse("profiles_index")
    assert path == "/profiles/"
    response = client.get(path)
    content = response.content.decode()
    expected_content = "<title>Profiles</title>"
    assert response.status_code == 200
    assert expected_content in content


@pytest.mark.django_db
def test_profile_url(client):
    User.objects.create(
        username="JohnDoe",
        first_name="John",
        last_name="Doe",
        email="johndoe@hotmail.com",
        password="unknow",
    )

    Profiles.objects.create(user=User.objects.get(id=1), favorite_city="Paris")

    path = reverse("profile", kwargs={"username": "JohnDoe"})
    assert path == "/profiles/JohnDoe/"
    response = client.get(path)
    content = response.content.decode()
    expected_content = "<title>JohnDoe</title>"
    assert response.status_code == 200
    assert expected_content in content
