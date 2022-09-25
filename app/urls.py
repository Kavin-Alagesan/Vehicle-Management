from django.urls import path
from app import views

urlpatterns=[
    path('register/',views.user_register,name="user_register"),
    path('signin/',views.user_signin,name="user_signin"),
    path('super_admin/',views.super_admin_func,name="super_admin_func"),
    path('admin_access/',views.admin_func,name="admin_func"),
    path('user_access/',views.user_func,name="user_func"),
    path('update_vehicle/<id>/',views.update_vehicle,name="update_vehicle"),
    path('list_role/',views.list_user_role,name="list_user_role"),
    path('list_type/',views.list_vehicle_type,name="list_vehicle_type"),
    path('update_user_role/<id>/',views.update_user_role,name="update_user_role"),
    path('update_type/<id>/',views.update_type,name="update_type"),

    path('delete_user_role/<id>/',views.delete_user_role,name="delete_user_role"),
    path('delete_vehicle/<id>/',views.delete_vehicle,name="delete_vehicle"),
    path('delete_type/<id>/',views.delete_type,name="delete_type"),

    path('signout/',views.user_logout,name="user_logout")

]

