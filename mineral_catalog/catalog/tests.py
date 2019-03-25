from django.urls import reverse
from django.test import TestCase

from .models import Minerals


class CatalogViewTests(TestCase):

    def setUp(self):
        self.mineral_test = Minerals.objects.create(
            name='Test Mineral',
            pk=123456
        )

    def test_catalog_mineral_list_view(self):
        resp = self.client.get(reverse('catalog:home'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral_test, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'catalog/mineral_list.html')
        for value in self.mineral:
            self.assertContains(resp, value.name)

    def test_catalog_mineral_detail_view(self):
        resp = self.client.get(reverse('catalog:detail',
                                       kwargs={'name': self.mineral_test.name,
                                               'pk': self.mineral_test.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'catalog/mineral_detail.html')
