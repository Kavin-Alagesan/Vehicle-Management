
from rest_framework import generics
from .models import *
from .serializer import *
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

# Create and update User
class UserCreateListAPI(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Create and update UserRole
class UserRoleListACreatePI(generics.ListCreateAPIView):
    # permission_classes = [AllowAny]
    permission_classes = (IsAuthenticated,)
    
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    
class UserRoleUpdateDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    # permission_classes = [AllowAny]

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserRoleListAPI(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    # permission_classes = [AllowAny]

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileNestedSerializer

class UserRolewithIDAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    # permission_classes = [AllowAny]

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileNestedSerializer

# Create and list vehicle type and vehicle details
class VehicleTypeListCreateAPI(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]

    queryset=VehicleTypeModel.objects.all()
    serializer_class=VehicleTypeSerializer

class VehicleDetailsListCreateAPI(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]

    queryset=VehicleModel.objects.all()
    serializer_class=VehicleSerializer

# List vehicle details
class VehicleList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]

    queryset=VehicleModel.objects.all()
    serializer_class=VehicleNestedSerializer

class VehicleListwithID(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]

    queryset=VehicleModel.objects.all()
    serializer_class=VehicleNestedSerializer

# Edit and Delete vehicle type and vehicle details
class VehicleTypeUpdateDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]

    queryset=VehicleTypeModel.objects.all()
    serializer_class=VehicleTypeSerializer

class VehicleDetailsUpdateDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]

    queryset=VehicleModel.objects.all()
    serializer_class=VehicleSerializer

# User login and logout
class LoginView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

