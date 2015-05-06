from rest_framework import serializers
from django.contrib.auth.models import User, Group
from resume.models import Resume, Experience, Qualification

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ('url', 'name')

class ExperienceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Experience

class QualificationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Qualification

class ResumeSerializer(serializers.ModelSerializer):
	qualification = QualificationSerializer(many=True)
	previous_experience = ExperienceSerializer()
	class Meta:
		model = Resume