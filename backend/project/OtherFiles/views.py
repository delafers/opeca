from django.shortcuts import render

from .serializers import FileSerializer
from .models import File
from rest_framework import generics


class GetFilesInfo(generics.ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
