from django.db import models

# Create your models here.
class user(models.Model):
	user_name = models.TextField(max_length = 50)
	password = models.TextField(max_length = 50)
	rating = models.IntegerField(default = 0)
	register_time = models.DateTimeField(null = True)


	def __unicode__(self):
		return self.user_name


class problem(models.Model):
	title = models.TextField(max_length = 200, default = None)
	description = models.TextField(max_length = 50000)
	input = models.TextField(max_length = 10000)
	output = models.TextField(max_length = 10000)
	sample_input = models.TextField(max_length = 10000)
	sample_output = models.TextField(max_length = 10000)
	source = models.TextField(max_length = 1000)
	manager = models.TextField(max_length = 1000)


class problemSubmit(models.Model):
	problemId = models.IntegerField(default = 0)
	language = models.IntegerField(default = 1)
	sourceCode = models.TextField(max_length = 200)
	md5 = models.TextField(max_length = 100)
	submiter = models.IntegerField(default = 0)
	status = models.IntegerField(default = 0)
	cost_time = models.IntegerField(null = True)
	cost_memory = models.IntegerField(null = True)
	code_length = models.IntegerField(null = True)
	submit_time = models.DateTimeField(null = True)

