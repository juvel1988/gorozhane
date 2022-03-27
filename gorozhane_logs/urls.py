from django.urls import include, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, re_path
from django.urls import path
from django.views.generic import TemplateView
from .views import  Index, Events

urlpatterns = [
     #Домашняя страница
    path('index/', Index.as_view(), name='index'), #Домашняя страница
    path('about/', TemplateView.as_view(template_name="about.html"), name='about'),
    path('contacts/', TemplateView.as_view(template_name="contacts.html"), name='contacts'),
    path('cooperate/', TemplateView.as_view(template_name="cooperate.html"), name='cooperate'),
    path (r'', views. articles, name = 'news'),#Лента новостей
    path('ckeditor/', include('ckeditor_uploader.urls')),#редактор статей
    path(r'new/<el_id>', views.el, name='el'),#Вывод отдельной новости
    ] 
