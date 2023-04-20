from .serializers import CryptoWalletsSerializer
from rest_framework import permissions
from rest_framework import viewsets
from .models import CryptoWallets


class CryptoWalletViewset(viewsets.ModelViewSet):
    queryset = CryptoWallets.objects.all()
    serializer_class = CryptoWalletsSerializer

    def get_permissions(self):
        if self.action == 'list':
            self.permission_classes = [IsSuperUser, ]
        elif self.action == 'retrieve':
            self.permission_classes = [IsSuperUser]
        return super(self.__class__, self).get_permissions()


class IsSuperUser(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_superuser


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user:
            if request.user.is_superuser:
                return True
            else:
                return obj.owner == request.user
        else:
            return False
