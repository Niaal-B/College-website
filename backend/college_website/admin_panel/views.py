from rest_framework import viewsets
from chatbot.serializers import ChatbotQASerializer
from chatbot.models import ChatbotQA
from feedback.models import Feedback
from feedback.serializers import FeedbackSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsSuperUser

from rest_framework import filters

class QuestionAnswerViewSet(viewsets.ModelViewSet):
    """ API to manage Q&A (CRUD) - Only for Superusers """
    queryset = ChatbotQA.objects.all()
    serializer_class = ChatbotQASerializer
    permission_classes = [IsAuthenticated, IsSuperUser]
    filter_backends = [filters.SearchFilter]
    search_fields = ["question", "answer"]  # Allows searching by question text

    def list(self, request, *args, **kwargs):
        print("User:", request.user)  # Debug user
        return super().list(request, *args, **kwargs)



class FeedbackViewSet(viewsets.ReadOnlyModelViewSet):
    """ API to View Feedback - Only for Superusers """
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated, IsSuperUser]  # Only logged-in superusers can access
