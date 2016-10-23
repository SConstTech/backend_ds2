from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework import generics, permissions, status, response, views
from rest_framework.response import Response
from rest_framework.reverse import reverse
from app.models import *


User = get_user_model()

# Create your views here.


class ProjectView(views.APIView):
    """
    Use this endpoint to logout user (remove user authentication token).
    """
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def post(self, request):
        receivedData = request.data

        try:
            projectID = receivedData['projectID']
        except KeyError:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)

        return response.Response(status=status.HTTP_204_NO_CONTENT)


class UserView(generics.RetrieveUpdateAPIView):
    """
    Use this endpoint to retrieve/update user.
    """
    model = User
    # serializer_class = serializers.serializers_manager.get('user')
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def get_object(self, *args, **kwargs):
        return self.request.user
