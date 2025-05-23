from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# NOTE THAT EACH CLASS SERVES AS A MODEL
class Post(models.Model):

	# class Status(models.TextChoices):
	# 	DRAFT = 'DF', 'Draft'
	# 	PUBLISHED = 'PB', 'Published'
	
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	# created = models.DateTimeField(auto_now_add=True)
	# updated = models.DateTimeField(auto_now=True)	
	"""In the above, i passed in auto_now=True which will put the current date and time the post was edited /updated
	and also i passed in auto_now_add=True which will put the current date and time only when the post was created
	but to be able to edit te date and time, timezone will be used imported from djang.utils"""
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
	# the on_delete is specifying what should be done when a user is deleted;
	# should the post be also deleted(which what CASCADE does), or leave it 

	# status = models.CharField(max_length=2,
	# 						choices=Status.choices,
	# 						default=Status.DRAFT)

	def __str__(self):
		return self.title


	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})


	# class Meta:
	# 	ordering = ['-date_posted']
	# 	indexes = [
	# 	models.Index(fields=['-date_posted']),
	# 	]