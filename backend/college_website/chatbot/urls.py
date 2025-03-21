from django.urls import path
from .views import ChatbotQAListView,ChatbotQAAdminView, ChatbotQADeleteView

urlpatterns = [
    path("chatbot-qa/", ChatbotQAListView.as_view(), name="chatbot-qa"),
    path("chatbot-admin/", ChatbotQAAdminView.as_view(), name="chatbot-admin"),
    path("chatbot-delete/<int:pk>/", ChatbotQADeleteView.as_view(), name="chatbot-delete"),
]
