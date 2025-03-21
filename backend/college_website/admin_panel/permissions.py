from rest_framework import permissions

class IsSuperUser(permissions.BasePermission):
    """
    Custom permission to allow only superusers to access the API.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_superuser
