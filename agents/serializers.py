from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Parking, Paiement
# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user 

# Parking Serializer
class ParkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parking
        fields = ('id', 'parkingName', 'parkingAddress', 'parkingPhone', 'parkingImage', 'parkingCapacity', 'parkingPrice')

    
# paiement Serializer
class PaiementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paiement
        fields = ('id', 'clientId', 'parking', 'duree', 'montant', 'date', 'periode')