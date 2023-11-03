from django.test import TestCase
from .models import Limit


class LimitModelTest(TestCase):
    def test_limit_creation(self):
        # Create a Limit instance
        limit = Limit.objects.create(emission_limit=1000)

        # Check if the instance was created successfully
        self.assertEqual(limit.emission_limit, 1000)

    def test_limit_string_representation(self):
        # Create a Limit instance
        limit = Limit.objects.create(emission_limit=2000)
        # Check if the __str__ method returns the expected string
        self.assertEqual(str(limit), "The emission limit is $2000")

    def test_limit_timestamps(self):
        # Create a Limit instance
        limit = Limit.objects.create(emission_limit=3000)

        # Check if created_at is not None
        self.assertIsNotNone(limit.created_at)

        # Check if updated_at is not None
        self.assertIsNotNone(limit.updated_at)

        # Check if updated_at is later than created_at
        self.assertGreater(limit.updated_at, limit.created_at)
