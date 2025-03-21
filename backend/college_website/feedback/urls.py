from django.urls import path
from .views import FeedbackCreateView,FeedbackAdminView

urlpatterns = [
    path("submit-feedback/", FeedbackCreateView.as_view(), name="submit-feedback"),
    path("feedback-admin/", FeedbackAdminView.as_view(), name="feedback-admin"),

]
