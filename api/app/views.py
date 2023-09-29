from django.shortcuts import render,HttpResponse
from .models import Student
from .serializers import StudentSerializer,UserSerializer
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
# Create your views here.

@csrf_exempt
def student(request):
    if request.method == 'GET':
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return JsonResponse(serializer.data,safe=False)

    elif request.method == 'POST':
        json_data=JSONParser().parse(request)
        serializer=StudentSerializer(data=json_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,safe=False)
        else:
            return JsonResponse(serializer.errors,safe=False)

    # return HttpResponse("This is ")

def user(request):
    user=User.objects.all()
    serializer=UserSerializer(user,many=True)
    return JsonResponse(serializer.data,safe=False)
    # return JsonResponse({"user":"this is "}) 


@csrf_exempt
def studentdetails(request,pk):
    try:
        student = Student.objects.get(pk=pk)

    except Student.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'Delete':
        student.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)




    elif request.method == 'GET':
        Serializer=StudentSerializer(student)
        # return JsonResponse("Student"+str(pk),safe=False)
        return JsonResponse(Serializer.data)

    elif request.method == 'PUT':
        # json_data = JSONParser().parse(request)
        json_data = request.POST
        serializer=StudentSerializer(data=json_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,safe=False)
        else:
            return JsonResponse(serializer.errors,safe=False) 