from rest_framework import routers
from django.urls import path, include
from .views import UserViewSet, PostViewSet, CommentViewSet

route = routers.DefaultRouter()
route.register(r'users', UserViewSet, 'views')
route.register(r'posts', PostViewSet, 'posts')
route.register(r'comments', CommentViewSet, 'comments')

urlpatterns = [
    path('', include(route.urls)),
]
