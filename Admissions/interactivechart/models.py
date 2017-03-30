from django.db import models

# Create your models here.
class Student(models.Model):
	ethnicity = models.CharField(max_length=100)
	gender = models.CharField(max_length=100)
	residency = models.CharField(max_length=100)
	college = models.CharField(max_length=100)
	headcount = models.IntegerField()
	year = models.IntegerField()
	# STATUS_CHOICES = ((APPLIED,'applied'), (ADMITTED, 'admitted'), (ENROLLED, 'enrolled'))

	def __str__(self):
		return self.year + ", " + self.headcount

"""class DataPoint(models.Model):
	student = models.ForeignKey(Student)
	year = student.year
	number = student.headcount"""

"""class Applied(model.Model):
	stats = models.ForeignKey(Status)
	APPLIED = 'applied'

class Admitted(model.Model):
	stats = models.ForeignKey(Status)
	ADMITTED = 'admitted'

class Enrolled(model.Model):
	stats = modles.ForeignKey(Status)
	ENROLLED = 'SIRed'
"""

