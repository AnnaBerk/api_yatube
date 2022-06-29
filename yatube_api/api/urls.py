from rest_framework.routers import DefaultRouter
from api.views import PostViewSet, GroupViewSet, CommentViewSet

v1_router = DefaultRouter()

v1_router.register('api/v1/posts', PostViewSet, basename='posts')
v1_router.register('api/v1/groups', GroupViewSet, basename='groups')
v1_router.register('api/v1/posts/(?P<post_id>\\d+)/comments', CommentViewSet,
                   basename='comments')
