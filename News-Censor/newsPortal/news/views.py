# views.py
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Article
from .filters import ArticleFilter

def index(request):
    return HttpResponse("Hello, world! This is the index page.")

def news_list(request):
    articles = Article.objects.all().order_by('-pub_date')  # Получаем все статьи
    paginator = Paginator(articles, 10)  # 10 статей на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)  # Получаем текущую страницу
    return render(request, 'news_list.html', {'page_obj': page_obj})  # Передаем в шаблон

def news_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'news_detail.html', {'article': article})

def news_search(request):
    articles = Article.objects.all()  # Получаем все статьи
    article_filter = ArticleFilter(request.GET, queryset=articles)  # Применяем фильтр
    return render(request, 'news_search.html', {'filter': article_filter})  # Передаем фильтр в шаблон
