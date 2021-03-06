# import json
# import os
import collections

from django.db.models import Q
from django.http import Http404
from django.shortcuts import render

from .models import Minerals


def mineral_list(request, letter='a'):
    minerals = Minerals.objects.filter(name__startswith=letter)
    minerals_group_raw = Minerals.objects.values('group').distinct()
    minerals_group = set(val for dic in minerals_group_raw
                         for val in dic.values())
    return render(request, 'catalog/mineral_list.html',
                  {'minerals': minerals,
                   'letter': 'A',
                   'minerals_group': minerals_group})


def mineral_list_sort_letter(request, letter=None):
    if not letter:
        letter = 'A'
    minerals = Minerals.objects.filter(name__startswith=letter)
    minerals_group_raw = Minerals.objects.values('group').distinct()
    minerals_group = set(val for dic in minerals_group_raw
                         for val in dic.values())
    return render(request, 'catalog/mineral_list.html',
                  {'minerals': minerals,
                   'letter': letter,
                   'minerals_group': minerals_group})


def mineral_list_sort_group(request, group):
    minerals = Minerals.objects.filter(group__icontains=group)
    minerals_group_raw = Minerals.objects.values('group').distinct()
    minerals_group = set(val for dic in minerals_group_raw
                         for val in dic.values())
    return render(request, 'catalog/mineral_list.html',
                  {'minerals': minerals,
                   'group': group,
                   'minerals_group': minerals_group})


def mineral_list_sort_hardness(request, hardness):
    minerals = Minerals.objects.filter(mohs_scale_hardness__icontains=hardness)
    minerals_group_raw = Minerals.objects.values('group').distinct()
    minerals_group = set(val for dic in minerals_group_raw
                         for val in dic.values())
    return render(request, 'catalog/mineral_list.html',
                  {'minerals': minerals,
                   'hardness': hardness,
                   'minerals_group': minerals_group})


def mineral_list_search_box(request):
    if request.method == 'GET':
        search_query = request.GET.get('search_box', None)
        minerals = Minerals.objects.filter(
            Q(name__icontains=search_query) |
            Q(image_caption__icontains=search_query) |
            Q(category__icontains=search_query) |
            Q(group__icontains=search_query) |
            Q(color__icontains=search_query) |
            Q(streak__icontains=search_query) |
            Q(diaphaneity__icontains=search_query) |
            Q(cleavage__icontains=search_query) |
            Q(formula__icontains=search_query) |
            Q(strunz_classification__icontains=search_query) |
            Q(crystal_system__icontains=search_query) |
            Q(unit_cell__icontains=search_query) |
            Q(crystal_symmetry__icontains=search_query) |
            Q(mohs_scale_hardness__icontains=search_query) |
            Q(luster__icontains=search_query) |
            Q(optical_properties__icontains=search_query) |
            Q(refractive_index__icontains=search_query) |
            Q(crystal_habit__icontains=search_query) |
            Q(specific_gravity__icontains=search_query))
    minerals_group_raw = Minerals.objects.values('group').distinct()
    minerals_group = set(val for dic in minerals_group_raw
                         for val in dic.values())
    return render(request, 'catalog/mineral_list.html',
                  {'minerals': minerals,
                   'minerals_group': minerals_group})


def mineral_detail(request, name, pk):
    try:
        minerals = Minerals.objects.filter(pk=pk)
        dict_minerals = collections.OrderedDict(Minerals.objects.filter(pk=pk)
                                                                .values()[0])
        minerals_group_raw = Minerals.objects.values('group').distinct()
        minerals_group = set(val for dic in minerals_group_raw
                             for val in dic.values())
    except Minerals.DoesNotExist:
        raise Http404("This page doesn't seem to exist")
    return render(request, 'catalog/mineral_detail.html',
                           {'minerals': minerals,
                            'dict_minerals': dict_minerals,
                            'minerals_group': minerals_group})


# def import_method(request):
#    filepath = os.path.dirname(__file__)
#    file_path = os.path.join(filepath, 'static/catalog/json/minerals.json')
#
#    with open(file_path, encoding="utf8") as json_file:
#        data = json.load(json_file)
#        for value in data:
#            value.setdefault('category', "")
#            value.setdefault('formula', "")
#            value.setdefault('strunz classification', "")
#            value.setdefault('color', "")
#            value.setdefault('crystal system', "")
#            value.setdefault('unit cell', "")
#            value.setdefault('crystal symmetry', "")
#            value.setdefault('cleavage', "")
#            value.setdefault('mohs scale hardness', "")
#            value.setdefault('luster', "")
#            value.setdefault('streak', "")
#            value.setdefault('diaphaneity', "")
#            value.setdefault('optical properties', "")
#            value.setdefault('refractive index', "")
#            value.setdefault('crystal habit', "")
#            value.setdefault('specific gravity', "")
#            value.setdefault('group', "")
#            d = Minerals(
#                name=value['name'],
#                image_filename=value['image filename'],
#                image_caption=value['image caption'],
#                category=value['category'],
#                formula=value['formula'],
#                strunz_classification=value['strunz classification'],
#                color=value['color'],
#                crystal_system=value['crystal system'],
#                unit_cell=value['unit cell'],
#                crystal_symmetry=value['crystal symmetry'],
#                cleavage=value['cleavage'],
#                mohs_scale_hardness=value['mohs scale hardness'],
#                luster=value['luster'],
#                streak=value['streak'],
#                diaphaneity=value['diaphaneity'],
#                optical_properties=value['optical properties'],
#                refractive_index=value['refractive index'],
#                crystal_habit=value['crystal habit'],
#                specific_gravity=value['specific gravity'],
#                group=value['group']
#            )
#            d.save()
#    return HttpResponse('Did it work?')
