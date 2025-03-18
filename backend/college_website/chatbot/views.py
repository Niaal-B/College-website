from rest_framework import generics
from .models import ChatbotQA
from .serializers import ChatbotQASerializer

class ChatbotQAListView(generics.ListAPIView):
    queryset = ChatbotQA.objects.all()
    serializer_class = ChatbotQASerializer
