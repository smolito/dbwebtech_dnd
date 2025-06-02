# characters/urls.py

from django.urls import path
from . import views # Importuje views z aktuální aplikace

app_name = 'characters' # Namespace pro URL, užitečné pro odkazování v šablonách

urlpatterns = [
    path('', views.home_page, name='home_page'), # Domovská stránka aplikace
    path('seznam/', views.postava_list, name='postava_list'), # URL pro seznam postav, např. /characters/seznam/
    path('postava/<int:pk>/', views.postava_detail, name='postava_detail'), # URL pro detail postavy, např. /characters/postava/1/
    path('postava/nova/', views.postava_create, name='postava_create')
]