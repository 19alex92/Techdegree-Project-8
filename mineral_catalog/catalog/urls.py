from django.urls import path

from . import views

app_name = 'catalog'
urlpatterns = [
    path('', views.mineral_list, name='home'),
    path('minerals/detail/<name>/<pk>', views.mineral_detail, name='detail'),
]
