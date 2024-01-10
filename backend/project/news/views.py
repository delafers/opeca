from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
from .serializers import NewsSerializer, NewsSerializerOld
from .models import News, NewsOld
from rest_framework import generics


class GetFiles(generics.ListAPIView):
    queryset = News.objects.all().order_by('id')
    serializer_class = NewsSerializer


class GetFilesNews(generics.ListAPIView):
    queryset = NewsOld.objects.all().order_by('id')
    serializer_class = NewsSerializerOld
