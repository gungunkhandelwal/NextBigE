import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth import get_user_model

# Test case for user registeration
@pytest.mark.django_db
def test_register():
    url=reverse('register')
    data = {
        'username': 'tester',
        'password': 'test123',
        'phone_number': '9876541210',
        'date_of_birth': '2024-05-01'
    }
    client = APIClient()
    response = client.post(url, data)
    assert response.status_code == 201

# Test case for user login
@pytest.mark.django_db
def test_login():
    user = get_user_model().objects.create_user(
        username='tester',
        password='test123',
        phone_number='9876541210',
        date_of_birth='2024-05-01'
    )
    url = reverse('login')
    data = {
        'username': 'tester',
        'password': 'test123'
    }
    client = APIClient()
    response = client.post(url, data)
    assert response.status_code == 200
    assert 'access' in response.data
    assert 'refresh' in response.data


# Test case for user profile
@pytest.mark.django_db
def test_profile():
    user = get_user_model().objects.create_user(
        username='tester',
        password='test123',
        phone_number='9876541210',
        date_of_birth='2024-05-01'
    )
    url = reverse('profile')
    client = APIClient()
    client.force_authenticate(user=user)
    response = client.get(url)
    assert response.status_code == 200
    assert response.data['username'] == 'tester'
    assert response.data['phone_number'] == '9876541210'