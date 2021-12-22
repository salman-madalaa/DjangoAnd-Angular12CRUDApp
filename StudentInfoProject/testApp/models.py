from django.db import models
from datetime import datetime
# Create your models here.

class Student(models.Model):
    rollNo = models.IntegerField()
    name = models.CharField(max_length=64)
    dob = models.DateTimeField(default=datetime.now, blank=True)
    marks = models.IntegerField(default = 200)
    email = models.EmailField(default='')
    phoneNumber = models.FloatField(default = 100)
    address = models.CharField(max_length=64)

    # def __init__(self, rollNo, name, dob, marks, email, phoneNumber, address):
    #     self.rollNo = rollNo
    #     self.name = name
	# 	self.dob = dob
	# 	self.marks = marks
	# 	self.email = email
	# 	self.phoneNumber = phoneNumber
	# 	self.address = address
