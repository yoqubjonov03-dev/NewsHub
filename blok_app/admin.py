from django.contrib import admin
from blok_app.models import Task, Comment
# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id','user__first_name','title', 'created_at')
    search_fields = ('title', )

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','title__id','rating')
    search_fields = ('title__title', )