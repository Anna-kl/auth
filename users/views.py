from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from requests import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.views import APIView

from users.serializers import UserSerializer

#permission_classes ((AllowAny,))
class CreateUserAPIView(APIView):
    permission_classes = (permissions.AllowAny,)

    #git remote add origin https://github.com/Anna-kl/auth.git@action(detail=False, methods=['post'], permission_classes=(permissions.IsAuthenticated,))
    def post(self,request):
        user=request.data
        serializer=UserSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)