fromd django.db import models

class PartFile(Models.model):
	fileId=models.TextField()
	partId=models.IntegerField()
	part=models.TextField()