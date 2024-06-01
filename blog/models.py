from django.db import models

# Create your models here.
class User(models.Model):
  username= models.CharField(max_length=15)
  email= models.CharField(max_length=30)
  password = models.CharField(max_length=50)

  def __str__(self) -> str:
    return self.username

class Post(models.Model):
  title= models.CharField(max_length=60)
  content= models.TextField()
  status= models.BooleanField(default=True)
  owner= models.ForeignKey(User, on_delete=models.CASCADE)
  created_at= models.DateTimeField(auto_now_add=True, editable=False)
  udpated_at= models.DateTimeField(auto_now=True)

  def __str__(self) -> str:
    return self.title

class Comment(models.Model):
  content= models.TextField()
  status= models.BooleanField(default=True)
  created_at= models.DateTimeField(auto_now_add=True, editable=False)
  udpated_at= models.DateTimeField(auto_now=True)
  author= models.ForeignKey(User, on_delete=models.CASCADE)
  post= models.ForeignKey(Post, on_delete=models.CASCADE)
