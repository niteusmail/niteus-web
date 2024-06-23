from django.shortcuts import render, get_object_or_404
from .models import Article, Menu, BasePage

def home(request):
    articles = Article.objects.all()
    menus = Menu.objects.prefetch_related('items').all()
    return render(request, 'blog/home.html', {'articles': articles, 'menus': menus})

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'blog/article_detail.html', {'article': article})

def base_page_detail(request, slug):
    page = get_object_or_404(BasePage, slug=slug)
    return render(request, 'blog/base_page_detail.html', {'page': page})

def custom_page_not_found(request, exception=None):
    return render(request, '404.html', status=404)
