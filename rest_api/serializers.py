from rest_framework import serializers
from blog.models import Post
from django.contrib.auth.models import User
from PIL import Image
from users.models import Profile


class PostSerializer(serializers.ModelSerializer):
	author_name = serializers.SerializerMethodField()
	author_pic_url = serializers.SerializerMethodField()

	class Meta:
		model = Post
		fields = ('id', 'url', 'title', 'content', 'date_posted', 'author', 'author_name', 'author_pic_url')

	def get_author_name(self, instance):
		return instance.author.username

	def get_author_pic_url(self, instance):
		return instance.author.profile.image.url

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username', 'email')


class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = ('user', )

