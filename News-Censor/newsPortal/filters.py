# filters.py
import django_filters
from .models import Article

class ArticleFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    author = django_filters.CharFilter(field_name='author__name', lookup_expr='icontains')  # Предполагается, что у вас есть поле author
    published_date = django_filters.DateFilter(field_name='pub_date', widget=django_filters.widgets.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Article
        fields = ['title', 'author', 'published_date']
