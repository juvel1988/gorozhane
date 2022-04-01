from django.urls import include, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, re_path
from django.urls import path
from django.views.generic import TemplateView
from .views import  Index

urlpatterns = [
     #Домашняя страница
    path('', Index.as_view(), name='index'), #Домашняя страница
    path('architecture/', TemplateView.as_view(template_name="architecture.html"), name='architecture'),#Архитектура
    path('sport/', TemplateView.as_view(template_name="sport.html"), name='sport'),#Спорт
    path('map/', TemplateView.as_view(template_name="map.html"), name='map'),#Карта
    path('culture/', TemplateView.as_view(template_name="culture.html"), name='culture'),#Культура
    path('excursions/', TemplateView.as_view(template_name="excursions.html"), name='excursions'),#Эксурсии

    path (r'afisha', views. articles, name = 'afisha'),#Лента новостей
    path('ckeditor/', include('ckeditor_uploader.urls')),#редактор статей
    path(r'new/<el_id>', views.el, name='el'),#Вывод отдельной новости
    ]