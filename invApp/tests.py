
from decimal import Decimal

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Product


class ProductViewsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="TestPassword123!"
        )

        self.client.login(
            username="testuser",
            password="TestPassword123!"
        )

        self.product = Product.objects.create(
            name="Test Laptop",
            sku="TEST-001",
            price=Decimal("500.00"),
            quantity=10,
            supplier="Test Supplier"
        )

    def test_product_list_view(self):
        response = self.client.get(reverse("product_list"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Laptop")

    def test_product_create_view(self):
        response = self.client.post(
            reverse("product_create"),
            {
                "name": "Test Mouse",
                "sku": "TEST-002",
                "price": "25.00",
                "quantity": 20,
                "supplier": "Test Supplier",
            }
        )

        self.assertRedirects(response, reverse("product_list"))

        self.assertTrue(
            Product.objects.filter(sku="TEST-002").exists()
        )

    def test_product_update_view(self):
        response = self.client.post(
            reverse("product_update", args=[self.product.product_id]),
            {
                "name": "Updated Laptop",
                "sku": "TEST-001",
                "price": "600.00",
                "quantity": 15,
                "supplier": "Updated Supplier",
            }
        )

        self.assertRedirects(response, reverse("product_list"))

        self.product.refresh_from_db()

        self.assertEqual(self.product.name, "Updated Laptop")
        self.assertEqual(self.product.price, Decimal("600.00"))

    def test_product_delete_view(self):
        response = self.client.post(
            reverse("product_delete", args=[self.product.product_id])
        )

        self.assertRedirects(response, reverse("product_list"))

        self.assertFalse(
            Product.objects.filter(
                product_id=self.product.product_id
            ).exists()
        )

    def test_inventory_requires_login(self):
        self.client.logout()

        response = self.client.get(reverse("product_list"))

        self.assertEqual(response.status_code, 302)
        self.assertIn("/login/", response.url)

