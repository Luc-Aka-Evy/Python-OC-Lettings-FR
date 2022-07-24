from django.test import TestCase
from django.urls import reverse
from .models import Letting, Address
import pytest


# Create your tests here.
@pytest.mark.django_db
def test_letting_url(client):
    Address.objects.create(
        number="94",
        street="Avenue de la république",
        city="Paris",
        state="IDF",
        zip_code="75001",
        country_iso_code="FR",
    )

    Letting.objects.create(title="This is Paris", address=Address.objects.get(id=1))

    path = reverse("letting", kwargs={"letting_id": 1})
    assert path == "/lettings/1/"
    response = client.get(path)
    content = response.content.decode()
    expected_content = "<title>This is Paris</title>"
    assert response.status_code == 200
    assert expected_content in content


@pytest.mark.django_db
def test_index_url(client):
    path = reverse("lettings_index")
    assert path == "/lettings/"
    response = client.get(path)
    content = response.content.decode()
    expected_content = "<title>Lettings</title>"
    assert response.status_code == 200
    assert expected_content in content
