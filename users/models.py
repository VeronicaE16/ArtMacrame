from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
	content = models.TextField()

	def __str__(self):
		return f'{self.user.username}: {self.content}'