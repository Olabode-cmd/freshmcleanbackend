from .models import User
from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.role == User.ROLE.ADMIN)
    

class IsAdminOrCleaner(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.role in [User.ROLE.ADMIN, User.ROLE.CLEANER])
    

class IsVerified(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.is_verified)

class IsActive(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.is_active)
    

