from rest_framework import permissions

class isOperator(permissions.BasePermission):
    """
    Global permission check if is operator.
    """
    def has_permission(self, request, view):
        return request.user.groups.filter(name='operators').exists()

class isClient(permissions.BasePermission):
    """
    Global permission check if is client.
    """
    def has_permission(self, request, view):
        return request.user.groups.filter(name='clients').exists()

class isAdmin(permissions.BasePermission):
    """
    Global permission check if is client.
    """
    def has_permission(self, request, view):
        return request.user.groups.filter(name='admin').exists()
