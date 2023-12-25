"""
Views for the user API.
"""
from rest_framework import generics, authentication, permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.views import APIView
from user.renderers import UserRenderer
from django.contrib.auth import authenticate
# from rest_framework_simplejwt.tokens import RefreshToken
from user.serializers import (
    UserSerializer,
    AuthTokenSerializer,
    # UserLoginSerializer,
)

# # Generate Token Manually
# def get_tokens_for_user(user):
#   refresh = RefreshToken.for_user(user)
#   return {
#       'refresh': str(refresh),
#       'access': str(refresh.access_token),
#   }

class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer

class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user."""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user."""
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve and return the authenticated user."""
        return self.request.user

# class UserRegistrationView(APIView):
#   renderer_classes = [UserRenderer]
#   def post(self, request, format=None):
#     serializer = UserRegistrationSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     user = serializer.save()
#     token = get_tokens_for_user(user)
#     return Response({'token':token, 'msg':'Registration Successful'}, status=status.HTTP_201_CREATED)

# class UserLoginView(APIView):
#   renderer_classes = [UserRenderer]
#   def post(self, request, format=None):
#     serializer = UserLoginSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     email = serializer.data.get('email')
#     password = serializer.data.get('password')
#     user = authenticate(email=email, password=password)
#     if user is not None:
#       token = get_tokens_for_user(user)
#       return Response({'token':token, 'msg':'Login Success'}, status=status.HTTP_200_OK)
#     else:
#       return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)

# class UserProfileView(APIView):
#   renderer_classes = [UserRenderer]
#   permission_classes = [IsAuthenticated]
#   def get(self, request, format=None):
#     serializer = UserProfileSerializer(request.user)
#     return Response(serializer.data, status=status.HTTP_200_OK)
