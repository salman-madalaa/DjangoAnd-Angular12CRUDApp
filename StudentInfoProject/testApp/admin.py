from django.contrib import admin
from testApp.models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display =['rollNo','name','dob','marks','email','phoneNumber','address'];

admin.site.register(Student,StudentAdmin)
