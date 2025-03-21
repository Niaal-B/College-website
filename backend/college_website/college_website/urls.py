from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),  # Default Django admin panel
    path("api/", include("chatbot.urls")),  # Chatbot-related APIs
    path("api/", include("feedback.urls")),  # Feedback-related APIs
    path("api/admin-dashboard/", include("admin_panel.urls")),  # Custom admin panel APIs
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),  # JWT Login
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),  # Refresh token
]
