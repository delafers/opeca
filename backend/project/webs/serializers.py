from rest_framework import serializers
from .models import Webinar


class WebinarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Webinar
        fields = ('header', 'img', 'ref')

