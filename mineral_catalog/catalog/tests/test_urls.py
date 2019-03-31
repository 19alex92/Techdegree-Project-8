from django.test import SimpleTestCase
from django.urls import reverse, resolve
from catalog.views import (mineral_list, mineral_list_sort_letter,
                           mineral_list_sort_group, mineral_list_sort_hardness,
                           mineral_list_search_box, mineral_detail)


class TestUrls(SimpleTestCase):

    def test_mineral_list_url_is_resolved(self):
        '''Tests if correct function is called when opened URL "home"'''
        url = reverse('catalog:home')
        self.assertEquals(resolve(url).func, mineral_list)

    def test_mineral_list_sort_letter_url_is_resolved(self):
        '''Tests if correct function is called when opened URL "sort_letter"'''
        url = reverse('catalog:sort_letter', args=['A'])
        self.assertEquals(resolve(url).func, mineral_list_sort_letter)

    def test_mineral_list_sort_group_url_is_resolved(self):
        '''Tests if correct function is called when opened URL "sort_group"'''
        url = reverse('catalog:sort_group', args=['SomeGroup'])
        self.assertEquals(resolve(url).func, mineral_list_sort_group)

    def test_mineral_list_sort_hardness_url_is_resolved(self):
        '''Tests if correct function is called '''
        '''when opened URL "sort_hardness"'''
        url = reverse('catalog:sort_hardness', args=['5'])
        self.assertEquals(resolve(url).func, mineral_list_sort_hardness)

    def test_mineral_list_search_box_url_is_resolved(self):
        '''Tests if correct function is called when opened URL "search"'''
        url = reverse('catalog:search')
        self.assertEquals(resolve(url).func, mineral_list_search_box)

    def test_mineral_list_detail_url_is_resolved(self):
        '''Tests if correct function is called when opened URL "detail"'''
        url = reverse('catalog:detail', kwargs={'name': 'SomeName',
                                                'pk': '2'})
        self.assertEquals(resolve(url).func, mineral_detail)
