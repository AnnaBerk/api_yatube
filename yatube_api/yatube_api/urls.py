from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.views import PostViewSet, GroupViewSet, CommentViewSet

router = DefaultRouter()

router.register('api/v1/posts', PostViewSet)
router.register('api/v1/groups', GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/v1/api-token-auth/', include('djoser.urls')),
    path('api/v1/api-token-auth', include('djoser.urls.jwt')),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
