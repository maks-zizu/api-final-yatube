from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Разрешает чтение всем, а изменение — только автору объекта."""

    def has_permission(self, request, view):
        # На уровне запроса: писать можно только будучи залогиненным
        return (
            request.method in permissions.SAFE_METHODS
            or request.user and request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        # На уровне объекта: только автор
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
