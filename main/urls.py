from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('add_review/<str:movie_title>/', views.add_review, name='add_review'),
    path('articles/', views.list_review, name='list_review'),
    path('delete_review/<int:article_id>/', views.delete_review, name='delete_review'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_URL)
