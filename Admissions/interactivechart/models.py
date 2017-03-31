from django.db import models

# Create your models here.
class Student(models.Model):
	ethnicity = models.CharField(max_length=100)
	gender = models.CharField(max_length=100)
	residency = models.CharField(max_length=100)
	college = models.CharField(max_length=100)
	headcount = models.IntegerField()
	year = models.CharField(max_length=20)
	status = models.CharField(max_length=20, default='')

	def __str__(self):
		return self.year + ", " + self.headcount

"""class DataPoint(models.Model):
	student = models.ForeignKey(Student)
	year = student.year
	number = student.headcount"""

class Applied(models.Model):
	stats = models.ForeignKey(Student)
	APPLIED = 'applied'

class Admitted(models.Model):
	stats = models.ForeignKey(Student)
	ADMITTED = 'admitted'

class Enrolled(models.Model):
	stats = models.ForeignKey(Student)
	ENROLLED = 'SIRed'

