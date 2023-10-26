from rest_framework import permissions


class IsPublic(permissions.BasePermission):
    """Кастомный класс для возможности доступа только к активным привычкам"""

    def has_object_permission(self, request, view, obj):
        if request.user.pk == obj.user.pk or obj.is_public is True:
            return True
        else:
            return False
