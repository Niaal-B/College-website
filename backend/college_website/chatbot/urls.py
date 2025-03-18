from django.urls import path
from .views import ChatbotQAListView

urlpatterns = [
    path("chatbot-qa/", ChatbotQAListView.as_view(), name="chatbot-qa"),
]
