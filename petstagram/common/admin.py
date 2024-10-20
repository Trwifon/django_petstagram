from django.contrib import admin

from petstagram.common.models import Comment, Like


@admin.register(Comment)
class ComentAdmin(admin.ModelAdmin):
    list_display = ['text', 'datetime']

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass
