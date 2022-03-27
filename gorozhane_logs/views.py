from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils import timezone
from django.contrib.syndication.views import Feed
import datetime
from .models import Events, User, Culture, Architecture
#_______________________________________________________________________________________
class Index(TemplateView):
    #Домашняя страница приложения
    template_name = 'index.html'

class Architecture(TemplateView):
    template_name = 'architecture.html'

 #_______________________________________________________________________________________


def articles(request):#Страница новостей
        afisha = Events.objects.order_by('-date_added') 
        context = {'afisha': afisha}
        return render(request, 'gorozhane/afisha.html', context)


def el(request, el_id): #Вывод отдельной новости
    news = Events.objects.get(id=el_id)
    context = {'afisha':afisha}
    return render(request, 'gorozhane/article.html', context)

def date(request):
    now = datetime.datetime.now()
    print("Date: "+ now.strftime("%Y-%m-%d")) #текущая дата


def index_view(request):
    return render(request, 'index.html')