from django_filters import rest_framework as filters
from django.db.models import Avg
from .models import Task

class TaskFilter(filters.FilterSet):
    min_rating = filters.NumberFilter(method='filter_min_rating')
    max_rating = filters.NumberFilter(method='filter_max_rating')

    class Meta:
        model = Task
        fields = ['min_rating', 'max_rating']

    def filter_min_rating(self, queryset, name, value):
        # Har bir Task ga o‘rtacha reyting (avg_rating) qo‘shamiz va filter qilamiz
        return queryset.annotate(avg_rating=Avg('reviews__score')).filter(avg_rating__gte=value)

    def filter_max_rating(self, queryset, name, value):
        return queryset.annotate(avg_rating=Avg('reviews__score')).filter(avg_rating__lte=value)
