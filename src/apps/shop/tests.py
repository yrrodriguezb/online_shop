from django.test import TestCase
from django.utils import translation
from .models import Category


class CategoryTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):                                     
        cls.category = Category.objects \
          .create(name="Tea")

    def test_string_representation(self):
        self.assertEqual(str(self.category), "Tea")

    def test_language_code(self):
        self.category.set_current_language('es')
        self.assertEqual(self.category.get_current_language(), self.category.language_code)

    def test_category_they_are_same(self):
        tea = Category.objects.get(
          translations__name='Tea'
        )

        self.assertEqual(self.category, tea)
        