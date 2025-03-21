from rest_framework import generics, permissions
from .models import Feedback
from .serializers import FeedbackSerializer

class FeedbackCreateView(generics.CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [permissions.AllowAny]  # ✅ Allows unauthenticated users

class FeedbackAdminView(generics.ListAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [permissions.IsAuthenticated]  # ✅ Only authenticated users can see feedback
