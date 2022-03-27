from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext_lazy as _
from django import forms

class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True, verbose_name='Информация о пользователе: ')
    avatar = models.ImageField(verbose_name='Аватар: ')

class Events(models. Model):
    title = models.CharField('Заголовок', max_length=250)
    slug = models.SlugField('Идентификатор', max_length=50,unique=True)
    author = models.ForeignKey ( User, on_delete=models.CASCADE, 
    related_name='Автор', null=True, blank=True)
    main_photo = models.ImageField('Постер', null = True, blank = True, upload_to='articles/images/main')
    anons = models.CharField(max_length=350)
    body = RichTextUploadingField(
                                    null=False,
                                    blank=False,
                                    # config_name='toolbar_Custom',
                                    external_plugin_resources=[(
                                        'youtube', 
                                        '/static/ckeditor/ckeditor/plugins/youtube/',
                                        'plugin.js',
                                      
                                    )],
                                    )
    #file = models.FileField(null = True, blank = True, upload_to='static/media/docs/')
    date_added = models.DateTimeField(auto_now_add=True)
   
    def __str__(self): # Возврат понятного отображения заголовка в панель администрирования
        return self.title

    class Meta:
        verbose_name = u"Новость"
        verbose_name_plural = u"Афиша" #Афиша

class Architecture(models. Model):
    title = models.CharField('Заголовок', max_length=250)
    slug = models.SlugField('Идентификатор', max_length=50,unique=True)
    main_photo = models.ImageField('Постер', null = True, blank = True, upload_to='articles/images/main')
    anons = models.CharField(max_length=350)
    body = RichTextUploadingField(
                                    null=False,
                                    blank=False,
                                    # config_name='toolbar_Custom',
                                    external_plugin_resources=[(
                                        'youtube', 
                                        '/static/ckeditor/ckeditor/plugins/youtube/',
                                        'plugin.js',
                                      
                                    )],
                                    )
    #file = models.FileField(null = True, blank = True, upload_to='static/media/docs/')
    date_added = models.DateTimeField(auto_now_add=True)
   
    def __str__(self): # Возврат понятного отображения заголовка в панель администрирования
        return self.title

    class Meta:
        verbose_name = u"Статья"
        verbose_name_plural = u"Архитектура" #Архитектура"

class Culture(models. Model):
    title = models.CharField('Заголовок', max_length=250)
    slug = models.SlugField('Идентификатор', max_length=50,unique=True)
    main_photo = models.ImageField('Постер', null = True, blank = True, upload_to='articles/images/main')
    anons = models.CharField(max_length=350)
    body = RichTextUploadingField(
                                    null=False,
                                    blank=False,
                                    # config_name='toolbar_Custom',
                                    external_plugin_resources=[(
                                        'youtube', 
                                        '/static/ckeditor/ckeditor/plugins/youtube/',
                                        'plugin.js',
                                      
                                    )],
                                    )
    #file = models.FileField(null = True, blank = True, upload_to='static/media/docs/')
    date_added = models.DateTimeField(auto_now_add=True)
   
    def __str__(self): # Возврат понятного отображения заголовка в панель администрирования
        return self.title

    class Meta:
        verbose_name = u"Статья"
        verbose_name_plural = u"Культура" #Культура"
