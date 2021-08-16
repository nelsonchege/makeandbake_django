from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import serializers

from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .serializers import BlogsSerializer
from .models import Blogs
# Create your views here.
@api_view(['GET'])
def said_hello(request):
    return Response('hello')

@api_view(['GET'])
def blogs_paths(request):
    blogs_urls={
        'List':'/blog-list/',
        'Create':'/blog-create/',
        'Update':'/blog-update/<str:pk>/',
        'Delete':'/blog-delete/<str:pk>/',
    }
    return Response(blogs_urls)


@api_view(['GET'])
def bloglist(request):
    blogs = Blogs.objects.all()
    serializers = BlogsSerializer(blogs, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def oneblog(request,pk):
    blogs = Blogs.objects.get(id=pk)
    serializers = BlogsSerializer(blogs, many=False)
    return Response(serializers.data)

@api_view(['POST'])
def createblog(request):
    serializers = BlogsSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['POST'])
def updateblog(request,pk):
    blogs = Blogs.objects.get(id=pk)
    serializers = BlogsSerializer(instance=blogs ,data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['DELETE'])
def deleteblog(request,pk):
    blogs = Blogs.objects.get(id=pk)
    blogs.delete()
    return Response('blog deleted')
