from django.db import models
from django.conf import settings
from django.utils import timezone

class Post (models.Model):       # here we defined that our object Post is a django model and has to be saved in database

	# now here we will be specifying the attributes of our object model!

	author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	def publish(self):
		self.published_date = timezone.now()
		self.save()
	def __str__(self):
		return self.title