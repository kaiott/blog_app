from django.shortcuts import render
from django.contrib.auth.models import User
from blog.models import Post
from users.models import Profile
from .serializers import PostSerializer, UserSerializer, ProfileSerializer
from rest_framework import viewsets, permissions

class PostView(viewsets.ModelViewSet):
	# /permissions/?groups=REPLACE_ID_HERE
	model = Post
	serializer_class = PostSerializer

	queryset = Post.objects.all().order_by('-date_posted')

	def get_queryset(self):
		"""
		Optionally restricts the returned posts to a given user,
		by filtering against a `user_id` query parameter in the URL.
		"""
		queryset = super().get_queryset()
		user_id = self.request.query_params.get('user_id', None)
		if user_id is not None:
			queryset = queryset.filter(author=user_id)
		max_count = self.request.query_params.get('max_count', None)
		if max_count is not None:
			queryset = queryset[:int(max_count)]

		return queryset

class ProfileView(viewsets.ModelViewSet):
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer

class UserView(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
