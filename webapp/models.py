from django.db import models

# Create your models here.
class students(models.Model):
	
	std_id = models.IntegerField()
	firstname = models.CharField(max_length=10)
	lastname = models.CharField(max_length=10)
	email = models.EmailField(max_length=30)
	
	def __str__(self):
		return self.firstname
	