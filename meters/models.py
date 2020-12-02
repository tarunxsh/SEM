from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Meter(models.Model):

	STATUS_CHOICES = (
	('active', 'active'),
	('inactive', 'inactive'),
	)

	m_id = models.AutoField(primary_key=True)
	owner = models.ForeignKey(User,on_delete=models.SET_NULL,related_name='meter',null=True)
	address =  models.TextField()
	registration_date =  models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='active')
	Totalreadings = models.IntegerField(default=0)


	class Meta:
		ordering = ('registration_date',)

	def __str__(self):
		return self.owner.username+'_'+str(self.m_id)


class Readings(models.Model):
	meter = models.ForeignKey(Meter,on_delete=models.CASCADE,related_name='readings')
	time_stamp = models.DateTimeField(auto_now_add=True)
	reading = models.IntegerField(default=0)

	# def __str__(self):
	# 	return self.reading|1
