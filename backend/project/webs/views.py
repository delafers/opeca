from django.shortcuts import render

from .serializers import WebinarSerializer
from .models import Webinar
from rest_framework import generics


class GetWebinars(generics.ListAPIView):
    queryset = Webinar.objects.all().order_by('id')
    serializer_class = WebinarSerializer
