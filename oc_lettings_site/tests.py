from django.urls import reverse

# Create your tests here.
def test_index_url(client):
    path = reverse("index")
    assert path == "/"
    response = client.get(path)
    content = response.content.decode()
    expected_content = "<title>Holiday Homes</title>"
    assert response.status_code == 200
    assert expected_content in content
