from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Follow, Group, Post

User = get_user_model()


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')
        read_only_fields = fields


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Post
        fields = (
            'id',
            'author',
            'text',
            'pub_date',
            'image',
            'group',
        )
        read_only_fields = ('id', 'author', 'pub_date')


class CommentSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = (
            'id',
            'author',
            'text',
            'created',
            'post',
        )
        read_only_fields = ('id', 'author', 'created', 'post')


class FollowSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(slug_field='username', read_only=True)
    following = SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        fields = ('user', 'following')

    def validate(self, data):
        request_user = self.context['request'].user
        following = data['following']

        if request_user == following:
            raise serializers.ValidationError(
                {'following': 'Нельзя подписаться на самого себя!'}
            )

        if Follow.objects.filter(
            user=request_user,
            following=following
        ).exists():
            raise serializers.ValidationError(
                {'following': 'Вы уже подписаны на этого пользователя.'}
            )
        return data
