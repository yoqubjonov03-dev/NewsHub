from rest_framework import serializers
from blok_app.models import Task, Comment


class TaskSerializer(serializers.ModelSerializer):
    comment_count = serializers.SerializerMethodField()
    class Meta:
        model = Task
        fields = ['id','user', 'title', 'comment_count', 'description', 'created_at']

    def get_comment_count(self, obj):

        return Comment.objects.filter(title=obj.id).count()

