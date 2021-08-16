from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import WatchlistSerializer, StreamingPlatformSerializer , ReviewSerializer
from .models import Watchlist , StreamingPlatform , Review


class ReviewList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer 


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class WatchListAV(APIView):
    def get(self,request):
        watchlist = Watchlist.objects.all()
        serializer = WatchlistSerializer(watchlist, many=True)
        return Response(serializer.data)
    def post(self,request):
         serializer = WatchlistSerializer(data= request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data)
         return Response(serializer.errors)
         

class DetailsAV(APIView):
    def get(self,request,pk):
        try:
            watchlist = Watchlist.objects.get(id=pk)
        except:
            return Response({"error":"nothing found"})
            
        serializer = WatchlistSerializer(watchlist, many=False)
        return Response(serializer.data)

    def put(request,pk):
        try:
            watchlist = Watchlist.objects.get(id=pk)
            serializer = WatchlistSerializer(watchlist,data= request.data)
        except:
            return Response({"error":"could not update "})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
        
class StreamingPlatformAV(APIView):
    
    def get(self, request):
        streamingplatform = StreamingPlatform.objects.all()
        serializer = StreamingPlatformSerializer(streamingplatform, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = StreamingPlatformSerializer(data= request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
        return Response(serializer.errors)

class SingleStreamingPlatformAV(APIView):
    def get(self,request,pk):
        try:
            streamingplatform = StreamingPlatform.objects.get(id=pk)
        except:
            return Response({"error":"nothing found"})
        serializer = StreamingPlatformSerializer(streamingplatform, many=False)
        return Response(serializer.data)

    def put(self,request,pk):
        try:
            streamingplatform = StreamingPlatform.objects.get(id=pk)
            serializer = StreamingPlatformSerializer(streamingplatform,data= request.data)
        except:
            return Response({"error":"could not update "})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    