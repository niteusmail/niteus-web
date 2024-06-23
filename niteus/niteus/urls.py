
from django.contrib import admin
from django.urls import path
from blog.views import home
from django.conf import settings
from django.conf.urls.static import static
from blog.views import home, article_detail
from blog.views import home, article_detail, base_page_detail



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('article/<int:article_id>/', article_detail, name='article_detail'),
    path('<slug:slug>/', base_page_detail, name='base_page_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
