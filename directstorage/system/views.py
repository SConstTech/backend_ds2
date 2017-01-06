from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.contrib.auth import get_user_model

from rest_framework import generics, permissions, status, response, views
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from . import serializers, settings, utils, signals

from permissions import isOperator


User = get_user_model()


class LoginView(utils.ActionViewMixin, generics.GenericAPIView):
    """
    Use this endpoint to obtain user authentication token.
    """
    serializer_class = serializers.serializers_manager.get('login')
    permission_classes = (
        permissions.AllowAny,
    )

    def action(self, serializer):
        token = utils.login_user(self.request, serializer.user)
        group = serializer.user.groups.first()
        token_serializer_class = serializers.serializers_manager.get('token_group')
        return Response(
            data=token_serializer_class({'token':token, 'group':group}).data,
            status=status.HTTP_200_OK,
        )


class LogoutView(views.APIView):
    """
    Use this endpoint to logout user (remove user authentication token).
    """
    permission_classes = (permissions.IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, )

    def post(self, request):
        utils.logout_user(request)
        return response.Response(status=status.HTTP_204_NO_CONTENT)


class UserView(generics.RetrieveUpdateAPIView):
    """
    Use this endpoint to retrieve/update user.
    """
    model = User
    serializer_class = serializers.serializers_manager.get('user')
    authentication_classes = (JSONWebTokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )

    def get_object(self, *args, **kwargs):
        return self.request.user