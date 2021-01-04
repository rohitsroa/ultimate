from django.db import models

# Create your models here.
class QueryInfo(models.Model):
	Name = models.CharField(max_length=50)
	Email = models.CharField(max_length=100)
	Phone = models.CharField(max_length=50)
	Service = models.CharField(max_length=100)
	Message = models.TextField(max_length=500)
	Date = models.DateTimeField(auto_now=True)
	Status = models.BooleanField()
	Engineer_Name = models.CharField(max_length=50)
	Manager_Name = models.CharField(max_length=50)

	def __str__(self):
		return self.Name