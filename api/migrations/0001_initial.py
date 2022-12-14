# Generated by Django 4.1.1 on 2022-09-23 05:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleTypeModel',
            fields=[
                ('vehicle_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('vehicle_type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleModel',
            fields=[
                ('vehicle_id', models.AutoField(primary_key=True, serialize=False)),
                ('vehicle_number', models.CharField(max_length=20)),
                ('vehicle_model', models.CharField(max_length=20)),
                ('vehicle_description', models.CharField(max_length=20)),
                ('vehicle_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.vehicletypemodel')),
            ],
        ),
    ]
