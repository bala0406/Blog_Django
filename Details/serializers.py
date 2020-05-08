from rest_framework import serializers
from .models import UserInformation

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInformation
        fields = [
            "name","about","email","phone","gender","currentuser"
        ]