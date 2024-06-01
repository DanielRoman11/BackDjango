from rest_framework import viewsets
from .serializers import UserSerializer, PostSerializer, CommentSerializer
from .models import User, Post, Comment

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
  serializer_class= UserSerializer()
  queryset= User.objects.all()

class PostViewSet(viewsets.ModelViewSet):
  serializer_class= PostSerializer()
  queryset= Post.objects.all()

class CommentViewSet(viewsets.ModelViewSet):
  serializer_class= CommentSerializer()
  queryset= Comment.objects.all()
