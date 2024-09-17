from django.urls import path

from . import views

urlpatterns = [
    path("", views.all, name="all"),
    path("news/", views.news, name="news"),
    path('news/<int:news_id>/', views.detailnews, name='detailnews'),
]