from rest_framework import serializers
from .models import *


class EmotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emotions
        fields = "__all__"
        # fields = ['Id','emotion']


class CreateEmotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emotions
        fields = ["emotion"]


class UpdateEmotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emotions
        fields = ["Id", "emotion"]
