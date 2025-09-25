from rest_framework import viewsets
from blok_app.models import Comment
from blok_app.serializers import CommentSerializer
from rest_framework.pagination import PageNumberPagination
from blok_app.permissions import CommentPermissions
from rest_framework.permissions import IsAuthenticated
class CommentPagination(PageNumberPagination):
    page_size = 5


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes = [CommentPermissions]
    serializer_class = CommentSerializer
    pagination_class = CommentPagination