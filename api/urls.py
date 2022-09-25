from django.urls import path
from api.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.views import TokenBlacklistView

urlpatterns=[
    path('create_user/', UserCreateListAPI.as_view()),
    path('manage_user/', UserRoleListACreatePI.as_view()),
    path('manage_user/<int:pk>/', UserRoleUpdateDeleteAPI.as_view()),
    path('user_role/', UserRoleListAPI.as_view()),
    path('user_role/<int:pk>/', UserRolewithIDAPI.as_view()),
    path('create_vehicle_type/', VehicleTypeListCreateAPI.as_view()),
    path('create_vehicle/', VehicleDetailsListCreateAPI.as_view()),
    path('list_vehicle/', VehicleList.as_view()),
    path('list_vehicle/<int:pk>/', VehicleListwithID.as_view()),
    path('manage_vehicle_type/<int:pk>/', VehicleTypeUpdateDeleteAPI.as_view()),
    path('manage_vehicle/<int:pk>/', VehicleDetailsUpdateDeleteAPI.as_view()),
    path('token/',TokenObtainPairView.as_view()),
    path('token/refresh/',TokenRefreshView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', TokenBlacklistView.as_view()),
]
