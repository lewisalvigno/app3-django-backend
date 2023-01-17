# Generated by Django 4.1.4 on 2023-01-15 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agents', '0002_delete_parking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parkingName', models.CharField(max_length=100)),
                ('parkingAddress', models.CharField(max_length=100)),
                ('parkingPhone', models.CharField(max_length=100)),
                ('parkingImage', models.ImageField(upload_to='images/')),
                ('parkingCapacity', models.CharField(max_length=100)),
                ('parkingPrice', models.CharField(max_length=100)),
            ],
        ),
    ]