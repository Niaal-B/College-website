from rest_framework import generics, permissions
from .models import ChatbotQA
from .serializers import ChatbotQASerializer

# Allow Everyone to List Q&A
class ChatbotQAListView(generics.ListAPIView):
    queryset = ChatbotQA.objects.all()
    serializer_class = ChatbotQASerializer
    permission_classes = [permissions.AllowAny]  # No authentication required

# Admin-Only: Add New Q&A
class ChatbotQAAdminView(generics.ListCreateAPIView):
    queryset = ChatbotQA.objects.all()
    serializer_class = ChatbotQASerializer
    permission_classes = [permissions.IsAuthenticated]  # Admin-only access

# Admin-Only: Delete Q&A
class ChatbotQADeleteView(generics.DestroyAPIView):
    queryset = ChatbotQA.objects.all()
    serializer_class = ChatbotQASerializer
    permission_classes = [permissions.IsAuthenticated]
