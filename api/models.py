from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    USER_ROLE=(
        ('SUPER_ADMIN','SUPER_ADMIN'),
        ('ADMIN','ADMIN'),
        ('USER','USER'),
    )
    user=models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    role=models.CharField(max_length=25,choices=USER_ROLE)

    def __str__(self):
        return f"{self.user} : {self.role}"

# -----vehicle-----
class VehicleTypeModel(models.Model):
    vehicle_type_id=models.AutoField(primary_key=True)
    vehicle_type=models.CharField(max_length=25)

    def __str__(self):
        return self.vehicle_type

class VehicleModel(models.Model):
    vehicle_id=models.AutoField(primary_key=True)
    vehicle_number=models.CharField(max_length=25)
    vehicle_type_id=models.ForeignKey(VehicleTypeModel,on_delete=models.CASCADE)
    vehicle_model=models.CharField(max_length=50)
    vehicle_description=models.CharField(max_length=250)

    def __str__(self):
        return f"{self.vehicle_number} : {self.vehicle_model}"


