from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GroupViewSet, PostViewSet, CommentViewSet, FollowViewSet


v1_router = DefaultRouter()
v1_router.register('posts', PostViewSet, basename='posts')
v1_router.register('groups', GroupViewSet, basename='groups')
v1_router.register(r'posts/(?P<post_id>[^/.]+)/comments',
                   CommentViewSet, basename='comment')
v1_router.register('follow', FollowViewSet)


urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
