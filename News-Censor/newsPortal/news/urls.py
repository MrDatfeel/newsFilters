# urls.py
from django.urls import path
from .views import news_list, news_search, NewsCreate, ArticleCreate  # Импортируйте необходимые представления

urlpatterns = [
    path('', news_list, name='news_list'),  # Маршрут для списка новостей
    path('news/', news_list, name='news_list'),  # Маршрут для списка новостей
    path('news/search/', news_search, name='news_search'),  # Маршрут для поиска новостей
    path('news/create/', NewsCreate.as_view(), name='news_create'),  # Маршрут для создания новостей
    path('articles/create/', ArticleCreate.as_view(), name='article_create'),  # Маршрут для создания статей
]
