# characters/urls.py

from django.urls import path
from . import views # Importuje views z aktuální aplikace

app_name = 'characters' # Namespace pro URL, užitečné pro odkazování v šablonách

urlpatterns = [
    path('', views.home_page, name='home_page'), # Domovská stránka aplikace
    path('seznam/', views.postava_list, name='postava_list'), # seznam postav, např. /characters/seznam/
    path('postava/<int:pk>/', views.postava_detail, name='postava_detail'), # detail postavy, např. /characters/postava/1/
    path('postava/nova/', views.postava_create, name='postava_create'), # vytvoření nové postavy, např. /characters/postava/nova/
    path('postava/<int:pk>/upravit/', views.postava_update, name='postava_update'), # úprava existující postavy, např. /characters/postava/1/upravit/
    path('postava/<int:pk>/smazat/', views.postava_delete, name='postava_delete') # smazání postavy, např. /characters/postava/1/smazat/
]