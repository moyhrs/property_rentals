from django.urls import reverse
from django.test import RequestFactory
from .views import index
import pytest

@pytest.mark.django_db
def test_index():
    # Create a request factory
    request_factory = RequestFactory()
    
    # Create a request
    request = request_factory.get(reverse('index'))  # Assuming 'index' is the name of the URL pattern for the index view
    
    # Call the index view
    response = index(request)
    
    # Assert the response status code
    assert response.status_code == 200