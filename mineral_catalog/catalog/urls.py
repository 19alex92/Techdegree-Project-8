from django.urls import path

from . import views

app_name = 'catalog'
urlpatterns = [
    path('', views.mineral_list, name='home'),
    path('group/<group>', views.mineral_list_sort_group, name='sort_group'),
    path('hardness/<hardness>', views.mineral_list_sort_hardness, name='sort_hardness'),
    path('<letter>', views.mineral_list_sort_letter, name='sort_letter'),
    path('search/', views.mineral_list_search_box, name='search'),
    path('minerals/detail/<name>/<pk>', views.mineral_detail, name='detail'),
]
