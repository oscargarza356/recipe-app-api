from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


#rest_framework helper tools
from rest_framework.test import APIClient
from rest_framework import status

#first add a helper function or constant variable for urls

#constant are UPPERCASE
CREATE_USER_URL = reverse('user:create')
TOKEN_URL = reverse('user:token')

#helper user to create user you are testing with in database
def create_user(**params):
    return get_user_model().objects.create_user(**params)


class PublicUserApiTests(TestCase):
    """Test the user API (public)"""

    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user_success (self):
        """Test creating user with valid payload is successfull"""
        payload = {
            'email' : 'oscar@lgs.com',
            'password' : 'testpass',
            'name' : 'Oscar',
        }
        res = self.client.post(CREATE_USER_URL, payload)

        #checks to see the page load
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        #here we will get the user from the database and we will compaere it
        #to the one we created in the database
        user = get_user_model().objects.get(**res.data)
        self.assertTrue(user.check_password(payload['password']))

        #check password is not passed in the objects
        self.assertNotIn('password', res.data)

    def test_user_exists(self):
        """Test creating user that already exits"""
        payload = {
            'email' : 'oscar@lgs.com',
            'password' : 'testpass',
        }
        create_user(**payload)

        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        """Test that password is more than 5 chars"""
        payload = {
            'email' : 'oscar@lgs.com',
            'password' : 'pw',
            'name' : 'Oscar',
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(
            email = payload['email']
        ).exists()
        self.assertFalse(user_exists)


    def test_create_token_for_user(self):
        """Test that a token is created for the user"""
        payload = {'email': 'test@londonappadev.com', 'password': 'testpass'}
        create_user(**payload)
        res = self.client.post(TOKEN_URL, payload)
        #checks for key token in the response data we will assume the token
        #works as we are using the django function
        self.assertIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_token_invalid_credentials(self):
        """Test that the token is not created if invalid credentials are given"""
        create_user(email = 'test')
        payload = {'email': 'test@londonappadev.com', 'password': 'wrong'}
        res = self.client.post(TOKEN_URL, payload)

        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_no_user(self):
        """Test that token is not created if user doesn't exist"""
        payload = {'email': 'test@londonappadev.com', 'password': 'testpass'}
        res = self.client.post(TOKEN_URL, payload)
        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_toke_missing_field(self):
        """Test that email and password are required"""
        payload = {'email': 'one', 'password': ''}
        res = self.client.post(TOKEN_URL, payload)
        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
