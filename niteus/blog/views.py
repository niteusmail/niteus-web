
from django.shortcuts import render
from .models import Menu
from .models import Article
from .models import Article, Menu
from django.shortcuts import render, get_object_or_404

def menu_view(request):
    menus = Menu.objects.all()
    return render(request, 'menu.html', {'menus': menus})

def home(request):
    articles = Article.objects.all()
    menus = Menu.objects.prefetch_related('items').all()
    return render(request, 'blog/home.html', {'articles': articles, 'menus': menus})

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'blog/article_detail.html', {'article': article})
