from django.db import models

class gallery(models.Model):
	title = models.CharField(max_length=250, blank=True);
	description = models.CharField(max_length=1000, blank=True)
	file = models.FileField(max_length=250)
 
	def __str__(self):
		return 'Title : ' + self.title + ' ,' + 'Description : ' + self.description 
