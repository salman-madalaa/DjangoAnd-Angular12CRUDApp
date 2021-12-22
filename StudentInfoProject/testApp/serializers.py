from rest_framework import serializers
from testApp.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id',
                  'rollNo',
                  'name',
                  'dob',
                  'marks',
                  'email',
                  'phoneNumber',
                  'address',
        )





    # rollNo = serializers.IntegerField();
    # name = serializers.CharField(required=True,allow_blank=False ,max_length=64);
    # dob = serializers.DateField(required=True,allow_blank=False)
    # marks = serializers.IntegerField();
    # email = serializers.EmailField();
    # phoneNumber = serializers.IntegerField();
    # address = serializers.CharField(max_length=64)
    #
    #
    # def Create(self,validated_data):
    #     return Student.objects.Create(**validated_data);
    #
    # def Update(self,instance,validated_data):
    #     instance.rollNo = validated_data.get('rollNo',instance.rollNo)
    #     instance.name = validated_data.get('name',instance.name)
    #     instance.dob = validated_data.get('dob',instance.dob)
    #     instance.marks = validated_data.get('marks',instance.marks)
    #     instance.email = validated_data.get('email',instance.email)
    #     instance.phoneNumber = validated_data.get('phoneNumber',instance.phoneNumber)
    #     instance.address = validated_data.get('address',instance.address)
    #     instance.save()
    #     return instance;
