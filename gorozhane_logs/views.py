from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils import timezone
from django.contrib.syndication.views import Feed
import datetime
from .models import Events,  User
#_______________________________________________________________________________________
class Index(TemplateView):
    #Домашняя страница приложения
    template_name = 'index.html'
#_______________________________________________________________________________________



def articles(request):#Страница новостей
        news = Events.objects.order_by('-date_added') 
        context = {'news': news}
        return render(request, 'gorozhane/news.html', context)


def el(request, el_id): #Вывод отдельной новости
    news = News.objects.get(id=el_id)
    context = {'news':news}
    return render(request, 'gorozhane/article.html', context)

def date(request):
    now = datetime.datetime.now()
    print("Date: "+ now.strftime("%Y-%m-%d")) #текущая дата


def index_view(request):
    return render(request, 'index.html')