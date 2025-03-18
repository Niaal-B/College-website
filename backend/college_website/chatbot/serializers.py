from rest_framework import serializers
from .models import ChatbotQA

class ChatbotQASerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatbotQA
        fields = "__all__"
