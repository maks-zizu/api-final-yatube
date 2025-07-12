from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()
router.register('v1/posts', PostViewSet, basename='posts')
router.register('v1/groups', GroupViewSet, basename='groups')
router.register('v1/follow', FollowViewSet, basename='follow')

# нестовые комментарии
comments = CommentViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
comment_detail = CommentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('', include(router.urls)),
    path(
        'v1/posts/<int:post_id>/comments/',
        comments,
        name='comments'
    ),
    path(
        'v1/posts/<int:post_id>/comments/<int:pk>/',
        comment_detail,
        name='comment_detail'
    ),
    # JWT-аутентификация djoser + simplejwt
    path('v1/', include('djoser.urls.jwt')),
]
