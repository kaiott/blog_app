from django.shortcuts import render
from django.contrib.auth.models import User
from blog.models import Post
from users.models import Profile
from .serializers import PostSerializer, UserSerializer, ProfileSerializer
from rest_framework import viewsets

class PostView(viewsets.ModelViewSet):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class ProfileView(viewsets.ModelViewSet):
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer

class UserView(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
