from rest_framework import serializers
from .models import Meeting


class MeetingSerializerOut(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = ["id", "created_by", "category"]
