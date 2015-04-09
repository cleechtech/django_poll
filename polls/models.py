from django.db import models

# Create your models here.

class Question(models.Model):
	# each class variable represents a database field in the model
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	# string representation
	def __str__(self):
		return self.question_text


class Choice(models.Model):
	# each choice is related to a single Question
	question = models.ForeignKey(Question)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text


