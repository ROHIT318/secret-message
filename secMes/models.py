from django.db import models
from django.conf import settings

# Create your models here.
class message(models.Model):
	mid = models.AutoField(primary_key=True)
	username = models.CharField(max_length=30, blank=False)
	msg = models.CharField(max_length=1024, blank=False)
	time = models.DateField()

	def __str__(self):
		return self.msg
	