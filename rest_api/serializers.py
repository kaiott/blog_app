from rest_framework import serializers
from blog.models import Post
from django.contrib.auth.models import User
from PIL import Image
from users.models import Profile

class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = ('id', 'url', 'title', 'content', 'date_posted', 'author')

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username', 'email')

class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = ('user',)

