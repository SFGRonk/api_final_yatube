from django.urls import path, include
from rest_framework import routers

from .views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet


router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
                basename='comment')
router.register(r'groups', GroupViewSet)
router.register(r'follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
]
