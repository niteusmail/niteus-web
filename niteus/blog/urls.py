# blog/urls.py

from django.urls import path
from .views import home, article_detail, base_page_detail

urlpatterns = [
    path('', home, name='home'),
    path('article/<int:article_id>/', article_detail, name='article_detail'),
    path('<slug:slug>/', base_page_detail, name='base_page_detail'),
]
