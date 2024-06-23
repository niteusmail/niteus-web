from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class Menu(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200, blank=True, null=True)
    page = models.ForeignKey('BasePage', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    text = CKEditor5Field('Text', config_name='default')  # Использование CKEditor для текстового поля
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title

class BasePage(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = CKEditor5Field('Content', config_name='default')  # Использование CKEditor для текстового поля

    def __str__(self):
        return self.title
