from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.core.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email' , 'password']
        extra_kwargs= {
            'password' : {'write_only' : True}
        }
    
    def create(self, validated_data):
        user = User.objects.create(
        email = validated_data['email'],
        username = validated_data['username'],
        password = make_password(validated_data['password']),
        )
        return user
    
    def validate(self,data):
        if data.get('username'):
            username2=data.get('username')
            username_qs=User.objects.filter(username=username2)
            if username_qs.exists():
                raise ValidationError({'username':'Username already exists.Try different username.'})
        if data.get('email'):
            email2=data.get('email')
            email_qs=User.objects.filter(email=email2)
            if email_qs.exists():
                raise ValidationError({'email':'Email already exists.Try different email.'})
        if data.get('username'):
            username_qs=data.get('username')
            if (username_qs == ""):
                raise serializers.ValidationError({'username':'Username should not be empty'})
        if data.get('email'):
            email_qs=data.get('email')
            if (email_qs == ""):
                raise serializers.ValidationError({'email':'Email should not be empty'})
        if data.get('password'):
            password_qs=data.get('password')
            if (password_qs == ""):
                raise serializers.ValidationError({'password':'Password field should not be empty'})
        return data

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user', 'role']

    def validate(self,data):
        if data.get('user'):
            user_qs=data.get('user')
            if (user_qs == "0"):
                raise serializers.ValidationError({'user':'Username should select'})
        if data.get('role'):
            role_qs=data.get('role')
            if (role_qs == "0"):
                raise serializers.ValidationError({'role':'Role should select'})
        return data


class UserProfileNestedSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    class Meta:
        model = UserProfile
        fields = ['user', 'role']

# -----vehicle-----
class VehicleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=VehicleTypeModel
        fields=['vehicle_type_id','vehicle_type']

    def validate(self,data):
        if data.get('vehicle_type'):
            vehicle_type_qs=data.get('vehicle_type')
            if (vehicle_type_qs == ""):
                raise serializers.ValidationError({'vehicle_type':'Vehicle type field empty.'})
        return data    

# Nested Serializers
class VehicleNestedSerializer(serializers.ModelSerializer):
    vehicle_type_id=VehicleTypeSerializer()

    class Meta:
        model=VehicleModel
        fields=['vehicle_id','vehicle_number','vehicle_type_id','vehicle_model','vehicle_description']

# Nonnested Serializers
class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model=VehicleModel
        fields=['vehicle_id','vehicle_number','vehicle_type_id','vehicle_model','vehicle_description']

    def validate(self,data):
        if data.get('vehicle_number'):
            vehicle_number_qs=data.get('vehicle_number')
            if (vehicle_number_qs == ""):
                raise serializers.ValidationError({'vehicle_number':'Vehicle number should be filled.'})
        if data.get('vehicle_type_id'):
            vehicle_type_id_qs=data.get('vehicle_type_id')
            if (vehicle_type_id_qs == "0"):
                raise serializers.ValidationError({'vehicle_type_id':'Vehicle type should select.'})
        if data.get('vehicle_model'):
            vehicle_model_qs=data.get('vehicle_model')
            if (vehicle_model_qs == ""):
                raise serializers.ValidationError({'vehicle_model':'Vehicle model should select.'})
        if data.get('vehicle_description'):
            vehicle_description_qs=data.get('vehicle_description')
            if (vehicle_description_qs == ""):
                raise serializers.ValidationError({'vehicle_description':'Description should be filled.'})
        return data

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self,attr):
        data=super().validate(attr)
        token=self.get_token(self.user)
        data['user']=str(self.user)
        data['id']=self.user.id
        userprofobj=UserProfile.objects.get(user=self.user)
        data['role']=userprofobj.role
        return data

        