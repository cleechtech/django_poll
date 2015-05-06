from django.db import models

class Qualification(models.Model):
	name = models.CharField(max_length=75)

	def __unicode__(self):
		return self.name

class Experience(models.Model):
	title = models.CharField(max_length=150)
	start_date = models.DateField()
	end_date = models.DateField()
	description = models.TextField()

	def __unicode__(self):
		return self.title

class Resume(models.Model):
	name = models.CharField(max_length=100)
	email = models.CharField(max_length=150)
	github_account = models.CharField(max_length=75)
	qualification = models.ManyToManyField(Qualification, related_name="qualification", null=True, blank=True)
	previous_experience = models.ForeignKey(Experience, related_name="experience")

	def __unicode__(self):
		return self.name