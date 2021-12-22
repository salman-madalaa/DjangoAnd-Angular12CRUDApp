from django.shortcuts import render
from django.http import HttpResponse
from testApp.models import Student
from django.http.response import JsonResponse
from testApp.serializers import StudentSerializer
from django.views.decorators.csrf import csrf_exempt
import json
from django.core import serializers
from rest_framework.parsers import JSONParser

# Create your views here.


def welcome(request):
    return render(request,"testApp/StudentInfo.html");

@csrf_exempt  # this method need not  cross site reference forgery
def allStudents(request):
    allStudents = Student.objects.all().order_by('-id');  # reverse order the data based in id
    # allStudents = Student.objects.filter(name__startswith ='A').order_by('-id');  # start with name 'A' reverse oreder the data based in id
    student_Serializer = StudentSerializer(allStudents, many=True)
    return JsonResponse(student_Serializer.data,safe=False);


@csrf_exempt
def newStudent(request):
    student_data=JSONParser().parse(request)
    student_serializer = StudentSerializer(data=student_data);
    print(student_serializer);
    if student_serializer.is_valid():
        student_serializer.save()
        return JsonResponse("Student Registered Successfully!!", safe=False);
    return JsonResponse("Failed to Add.",safe=False);

@csrf_exempt
def deleteStudent(request,id):
    student=Student.objects.get(pk=id)
    student.delete()
    return JsonResponse("Deleted Succeffully!!", safe=False)

@csrf_exempt
def getStudent(request,id):
    student = Student.objects.get(pk=id);
    student_Serializer = StudentSerializer(student, many=False);
    return JsonResponse(student_Serializer.data,safe=False);


@csrf_exempt
def updateStudent(request,id):
    student_data=JSONParser().parse(request);
    print(student_data);
    student = Student.objects.get(id=id);
    student_serializer = StudentSerializer(student,data=student_data);
    print(student_serializer);
    if student_serializer.is_valid():
        student_serializer.save()
        return JsonResponse("Student Updated Successfully!!", safe=False);
    return JsonResponse("Failed to Update.",safe=False);
