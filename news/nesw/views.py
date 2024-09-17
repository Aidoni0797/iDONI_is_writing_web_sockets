from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from .models import News
from django.shortcuts import render, get_object_or_404

def all(request):
    news = News.objects.all().order_by('-created_at')
    news_list = list(news.values('id', 'title', 'content', 'created_at'))
    return JsonResponse(news_list, safe=False)

def news(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detailnews(request, news_id):
    news = get_object_or_404(News, id=news_id)
    comments = news.comments.all()
    news_data = {
        'id': news.id,
        'title': news.title,
        'content': news.content,
        'created_at': news.created_at,
        'comments': list(comments.values('id', 'content', 'created_at'))
    }
    return JsonResponse(news_data)