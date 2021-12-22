
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'StudentInfoProject.settings')
import django
django.setup()

from testApp.models import *
from faker import Faker
from random import *
faker = Faker()


def phoneNumberGenerate():
    d1 = randint(6, 9)
    num = str(d1)
    for i in range(9):
        num = num + str(randint(0,9))  # here + means contatination
    return int(num)


def fakeStudentData(n):
    for i in range(n):
        frollno = faker.random_int(min=1, max=999)
        fname = faker.name()
        fdob = faker.date()
        fmarks = faker.random_int(min=1, max=100)
        femail = faker.email()
        fphoneNumber = phoneNumberGenerate()
        faddress = faker.address()
        student_record = Student.objects.get_or_create(
            rollNo=frollno, name=fname, dob=fdob, marks=fmarks, email=femail, phoneNumber=fphoneNumber, address=faddress)

fakeStudentData(49)
