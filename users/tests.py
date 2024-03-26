from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class UserRegistrationTest(TestCase):
    def test_registration_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')

        # Testing registration functionality
        data = {
            'username': 'testuser',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123'
        }
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful registration
        self.assertTrue(User.objects.filter(username='testuser').exists())

class UserProfileTest(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword123')

    def test_profile_view(self):
        self.client.login(username='testuser', password='testpassword123')
        response = self.client.get(reverse('editProfile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/editProfile.html')

        # Testing profile update functionality
        data = {
            'username': 'updatedusername',
            'first_name': 'Updated',
            'last_name': 'User',
            'email': 'updated@example.com'
        }
        response = self.client.post(reverse('editProfile'), data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful profile update
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'updatedusername')
        self.assertEqual(self.user.email, 'updated@example.com')

class ChangePasswordTest(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword123')

    def test_password_change_view(self):
        self.client.login(username='testuser', password='testpassword123')
        response = self.client.get(reverse('passwordChange'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/changePassword.html')

        # Testing password change functionality
        data = {
            'old_password': 'testpassword123',
            'new_password1': 'newtestpassword123',
            'new_password2': 'newtestpassword123'
        }
        response = self.client.post(reverse('passwordChange'), data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful password change
        self.assertTrue(self.client.login(username='testuser', password='newtestpassword123'))

