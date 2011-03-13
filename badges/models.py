from django.db import models
from django.contrib.auth.models import User

#class User(models.Model):
#	name = models.CharField(max_length=30)
#	provider = models.CharField(max_length=30)
#	token = models.CharField(max_length=100)
#
#	def __unicode__(self):
#		return self.name

class Badge(models.Model):
	name = models.CharField(max_length=30)
	photoUrl = models.CharField(max_length=100)
	description = models.CharField(max_length=400)

	def __unicode__(self):
		return self.name

class Rule(models.Model):
	owner = models.ForeignKey(User)
	query = models.CharField(max_length=400)
	minCount = models.IntegerField()
	badge = models.ForeignKey(Badge)

	def __unicode__(self):
		return self.query

class History(models.Model):
	date = models.DateTimeField("Data/Hora")
	user = models.ForeignKey(User)
	badge = models.ForeignKey(Badge)
	status = models.CharField(max_length=400)

	def __unicode__(self):
		return self.status
