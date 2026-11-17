
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Profile


class AuthenticationTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="StrongTestPass!2026"
        )

    def test_user_registration(self):
        response = self.client.post(
            reverse("register"),
            {
                "username": "newuser",
                "password": "StrongTestPass!2026",
                "password_confirm": "StrongTestPass!2026",
            }
        )

        self.assertRedirects(response, reverse("home"))
        self.assertTrue(
            User.objects.filter(username="newuser").exists()
        )

    def test_user_login(self):
        response = self.client.post(
            reverse("login"),
            {
                "username": "testuser",
                "password": "StrongTestPass!2026",
            }
        )

        self.assertRedirects(response, reverse("home"))

    def test_invalid_login(self):
        response = self.client.post(
            reverse("login"),
            {
                "username": "testuser",
                "password": "WrongPassword123!",
            }
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Invalid credentials")

    def test_user_logout(self):
        self.client.force_login(self.user)

        response = self.client.post(reverse("logout"))

        self.assertRedirects(response, reverse("login"))
        self.assertFalse(
            self.client.session.get("_auth_user_id")
        )

    def test_profile_requires_login(self):
        response = self.client.get(reverse("profile"))

        self.assertEqual(response.status_code, 302)
        self.assertIn("/login/", response.url)

    def test_profile_view(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse("profile"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/profile.html")
        self.assertTrue(
            Profile.objects.filter(user=self.user).exists()
        )

