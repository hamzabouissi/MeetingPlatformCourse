from rest_framework import serializers
from .models import Meeting
from Auth.models import User


class MeetingSerializerOut(serializers.ModelSerializer):
    class UserSerializerMicro(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ("id", "username", "email")

    created_by = UserSerializerMicro()

    class Meta:
        model = Meeting
        fields = ["id", "created_by", "category"]
