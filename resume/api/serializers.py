from rest_framework import serializers
from django.contrib.auth.models import User, Group
from resume.models import Resume, Experience

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ('url', 'name')

class ResumeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Resume

class ExperienceSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Experience