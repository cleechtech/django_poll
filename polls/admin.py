from django.contrib import admin

# import models from the current package
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
	model = Choice
	# provide enough fields for three choices
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
	# Reorder fields
	fields = ['pub_date', 'question_text']

	# Group fields
	fieldsets = []

	# Choice objects are edited on the
	# Question admin page
	inlines = [ChoiceInline]

	# fields to display as columns
	list_display = ('question_text', 'pub_date')

	# add filter sidebar
	list_filter = ['pub_date']

	# add search field
	search_fields = ['question_text']


# Register your models here.
admin.site.register(Question, QuestionAdmin)
