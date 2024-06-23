
from django.shortcuts import render
from .models import Menu
from .models import Article

def menu_view(request):
    menus = Menu.objects.all()
    return render(request, 'menu.html', {'menus': menus})

def home(request):
    articles = Article.objects.all()
    menus = Menu.objects.prefetch_related('items').all()
    return render(request, 'blog/home.html', {'articles': articles, 'menus': menus})
