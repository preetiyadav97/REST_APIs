from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers .Serializer):
    name=serializers.CharField(max_length=40)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=40)

    def create(self,validated_data):
        print("Creating Student....")
        return Student.objects.create(**validated_data)

    def update(self,student,validated_data):
        newemp = Student(**validated_data)
        newemp.id = Student.id
        newemp.save()
        return newemp




class UserSerializer(serializers .Serializer):
    username=serializers.CharField(max_length=40)
    email=serializers.EmailField()
    password=serializers.CharField(max_length=49)
    first_name=serializers.CharField(max_length=49)

    # roll=serializers.IntegerField()
    # phone=serializers.IntegerField()
    # city=serializers.CharField(max_length=40)


# # with the help of serializers we can convert python data in 
# json data