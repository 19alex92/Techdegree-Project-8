from django.urls import path

from . import views

app_name = 'catalog'
urlpatterns = [
    path('', views.mineral_list, name='home'),
    path('<letter>', views.mineral_list_sort_letter, name='letter'),
    path('minerals/detail/<name>/<pk>', views.mineral_detail, name='detail'),
]
