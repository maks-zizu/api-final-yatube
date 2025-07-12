from django.contrib import admin

from .models import Comment, Follow, Group, Post


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'pub_date', 'author', 'group')
    list_filter = ('pub_date', 'author', 'group')
    search_fields = ('text',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'post', 'created')
    list_filter = ('created',)
    search_fields = ('text',)


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('user', 'following')
