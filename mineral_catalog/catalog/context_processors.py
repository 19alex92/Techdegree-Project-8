from random import randint

from .models import Minerals


def add_variable_to_context(request):
    total_minerals = 0
    minerals = Minerals.objects.all()
    for value in minerals:
        total_minerals += 1
    random_number = randint(0, total_minerals)
    minerals = Minerals.objects.filter(pk=random_number)
    return {
        'random_mineral': minerals
    }
