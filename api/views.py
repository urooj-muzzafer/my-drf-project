from .models import student
from .serializers import studentserializer
from rest_framework.decorators import api_view
from rest_framework import viewsets
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def apiOverview(request):
    api_urls={
        'List of all tasks':'/tasks/',
        'Create New Task':'/tasks/',
        'Detail view':'/tasks/<id>',
    }
    return Response(api_urls)


@api_view(['GET','POST'])
def taskList(request):
    if request.method =='GET':
        tasks = student.objects.all().order_by('-id')
        serializer = studentserializer(tasks,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = studentserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','DELETE','PATCH'])
def taskDetail(request, pk):
    try:
        task = student.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = studentserializer(task)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_201_CREATED)
    elif request.method == 'PATCH':
        serializer = studentserializer(task, data=request.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
# class studentViewset(viewsets.ModelViewSet):
#     queryset = student.objects.all()
#     serializer_class = studentserializer
# @api_view(['GET','POST','DELETE'])
# def student_api(request):
#     if request.method == 'GET':

#         stu = student.objects.all()
#         serializer = studentserializer(stu,many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer = studentserializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     if request.method == 'DELETE':
#         student.delete()
#         return Response(status=status.HTTP_201_CREATED)