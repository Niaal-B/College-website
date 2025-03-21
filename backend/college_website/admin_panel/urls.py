from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuestionAnswerViewSet, FeedbackViewSet

# Create a router for handling API endpoints
router = DefaultRouter()
router.register(r'qa', QuestionAnswerViewSet)  # Q&A management (CRUD)
router.register(r'feedback', FeedbackViewSet)  # View feedback (Read-only)

urlpatterns = [
    path("", include(router.urls)),  # Include all registered routes
]
