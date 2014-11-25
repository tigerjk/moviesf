from django.db import models

# Create your models here.
class Movie(models.Model):
	title=models.TextField()
	release_year=models.IntegerField()
	locations=models.TextField()
	fun_facts=models.TextField()
	production_company=models.TextField()
	distributor=models.TextField()
	director=models.TextField()
	writer=models.TextField()
	actor_1=models.TextField()
	actor_2=models.TextField()
	actor_3=models.TextField()
