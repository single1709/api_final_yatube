from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from .views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet

v1_router = DefaultRouter()

app_name = 'api'

v1_router.register('posts', PostViewSet, basename='Post')
v1_router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='Post')
v1_router.register('groups', GroupViewSet, basename='Group')
v1_router.register('follow', FollowViewSet, basename='Follow')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
]
