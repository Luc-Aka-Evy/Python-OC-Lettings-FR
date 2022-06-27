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
        country_iso_code="FR"
        )

    Letting.objects.create(
        title="This is Paris",
        address=Address.objects.get(id=1)
        )
        
    path = reverse('letting', kwargs={'letting_id':1})
    response = client.get(path)
    content = response.content.decode()
    expected_content = "<h1>This is Paris</h1>"
    assert expected_content in content


@pytest.mark.django_db
def test_index_url(client):
    url = reverse('lettings_index')
    assert url == "/lettings/"
    response = client.get(url)
    content = response.content.decode()
    expected_content = "<h1>Lettings</h1>"
    assert expected_content in content

    
  
       
        