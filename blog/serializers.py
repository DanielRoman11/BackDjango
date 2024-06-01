from .models import Post, User, Comment
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model= User
    field= '__all__'

class PostSerializer(serializers.ModelSerializer):
  owner= UserSerializer(read_only=True)
  owner_id= serializers.PrimaryKeyRelatedField(write_only=True, queryset= User.objects.all(), source='owner')
  
  class Meta:
    model= Post
    field= '__all__'

class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model= Comment
    field= '__all__'