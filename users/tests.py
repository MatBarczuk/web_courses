from django.contrib.auth import get_user_model
from django.test import TestCase
from django.contrib.auth.models import Group
from django.urls import reverse


class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        Group.objects.create(name='student')
        user = User.objects.create_user(
            fullname='Mateusz',
            email='m@m.pl',
            password='testpass123'
        )

        self.assertEqual(user.fullname, 'Mateusz')
        self.assertEqual(user.email, 'm@m.pl')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        Group.objects.create(name='student')
        admin_user = User.objects.create_superuser(
            fullname='superadmin',
            email='m@m.pl',
            password='testpass123'
        )

        self.assertEqual(admin_user.fullname, 'superadmin')
        self.assertEqual(admin_user.email, 'm@m.pl')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class SignupPateTests(TestCase):

    fullname = 'new_user'
    email = 'new_user@email.com'

    def setUp(self):
        url = reverse('users:register')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'users/register.html')
        self.assertContains(self.response, 'Register here')
        self.assertNotContains(self.response, 'I should not be on the page')

    def test_signup_form(self):
        Group.objects.create(name='student')
        new_user = get_user_model().objects.create_user(
            fullname=self.fullname,
            email=self.email
        )

        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].fullname, self.fullname)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
