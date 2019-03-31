from django.test import TestCase

from catalog.models import Minerals


class TestModels(TestCase):

    def setUp(self):
        self.mineral = Minerals.objects.create(
            name='TestName',
            group='TestGroup',
            mohs_scale_hardness='5',
        )

    def test_mineral_creation(self):
        mineral = self.mineral
        self.assertTrue(isinstance(mineral, Minerals))
