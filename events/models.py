from django.db import models

# Create your models here.
class events(models.Model):
	name = models.CharField(max_length=50);
	team = models.CharField(max_length=50);
	
	def __str__(self):
		return ' Name ' + self.name  + 'Team : ' + self.team 

class students(models.Model):
	student_name = models.CharField(max_length=50);
	student_team = models.CharField(max_length=50);

	def __str__(self):
		return ' Name ' + self.student_name  + 'Team : ' + self.student_team