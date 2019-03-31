from django.test import TestCase, Client
from django.urls import reverse

from catalog.models import Minerals


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

        self.mineral = Minerals.objects.create(
            name='TestName',
            group='TestGroup',
            mohs_scale_hardness='5',
        )
        self.letter = 'A'

    def test_mineral_list(self):
        response = self.client.get(reverse('catalog:home'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/mineral_list.html')

    def test_mineral_list_sort_letter(self):
        response = self.client.get(reverse('catalog:sort_letter',
                                           kwargs={'letter': self.letter}))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/mineral_list.html')

    def test_mineral_list_sort_group(self):
        response = self.client.get(reverse('catalog:sort_group',
                                           kwargs={'group': self.mineral.group}
                                           ))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/mineral_list.html')

    def test_mineral_list_sort_hardness(self):
        response = self.client.get(reverse('catalog:sort_hardness',
                                           kwargs={'hardness':
                                                   self.mineral.mohs_scale_hardness}
                                           ))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/mineral_list.html')

    def test_mineral_list_search_box(self):
        response = self.client.get(reverse('catalog:search'),
                                   {'search_box': 'Te'})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/mineral_list.html')

    def test_mineral_detail(self):
        response = self.client.get(reverse('catalog:detail',
                                           kwargs={'name': self.mineral.name,
                                                   'pk': self.mineral.pk}))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/mineral_detail.html')
