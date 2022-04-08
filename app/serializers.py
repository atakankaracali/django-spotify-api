from rest_framework import serializers
from .models import music_app


class musicSerializer(serializers.ModelSerializer):
    class Meta:
        model = music_app
        fields = "__all__"
