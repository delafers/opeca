from rest_framework import serializers
from .models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('Header', 'description', 'img', 'date', 'text', 'ref')


class NewsSerializerOld(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('Header', 'description', 'img', 'date', 'text', 'ref')

