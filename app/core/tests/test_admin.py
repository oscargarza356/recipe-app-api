from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

class AdminSiteTests(TestCase):

    def setUp(self):
        # set up the client for future tests
        self.client = Client()
        # create a temporal admin
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@lgs.com',
            password = 'password123'
        )
        # sign the admin to the client
        self.client.force_login(self.admin_user)
        # create a user
        self.user = get_user_model().objects.create_user(
            email='test@lgs.com',
            password='password123',
            name='Test user full name'
        )

    def test_users_listed(self):
        """Test that users are listed on user page"""
        # get the url where you check users this urls are already built in django
        # it's kinda weird but it goes like app model action something like that look reverse docum
        # or at django admin url documentation
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)
        #check if the user exits
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """test that the user edit page work"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        # /admin/core/user/1
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """test that the user create page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
