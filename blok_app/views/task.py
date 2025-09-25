from django.db.models import Avg
from drf_yasg import openapi               #1
from drf_yasg.utils import swagger_auto_schema     #2
from rest_framework.pagination import PageNumberPagination
from  rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action
from blok_app.permissions import IsTaskPermission
from rest_framework.permissions import IsAuthenticated

from blok_app.models import Task
from blok_app.serializers import TaskSerializer
from blok_app.filters import TaskFilter
from django_filters import rest_framework as django_filter
from rest_framework import filters

class CustomPagination(PageNumberPagination):
    page_size = 4

class TaskViewSet(viewsets.ModelViewSet):
    queryset =Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [ IsTaskPermission]


    pagination_class = CustomPagination
    filter_backends = [django_filter.DjangoFilterBackend, filters.SearchFilter]
    filterset_class = TaskFilter
    search_fields = ['title','description']

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('min_rating', openapi.IN_QUERY, description="Minimum reyting", type=openapi.TYPE_NUMBER),
        openapi.Parameter('max_rating', openapi.IN_QUERY, description="Maximum reyting", type=openapi.TYPE_NUMBER),
    ])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @action(detail=False, methods=['get'])
    def top_rated(self, request):
        top_tasks = Task.objects.annotate(avg_rating=Avg('reviews__rating')).order_by('-avg_rating')[
                    :5]  # eng yuqori 5 ta
        serializer = self.get_serializer(top_tasks, many=True)
        return Response(serializer.data)