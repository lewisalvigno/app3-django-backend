from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer, ParkingSerializer, PaiementSerializer
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Parking, Paiement
import pusher

# get users from api


@api_view(['GET'])
def agent_list(request):

    # process:
    # get all the drink
    # serialize them
    # return json

    if request.method == 'GET':
        agents = User.objects.all()
        serializer = UserSerializer(agents, many=True) 
        return Response(serializer.data)


@api_view(['GET'])
def agent_specific(request, id):
    try:
        agent = User.objects.get(pk=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_401_NOT_FOUND)

    if request.method == "GET":
        serializer = UserSerializer(agent)
        return Response(serializer.data)


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

# get parkings


pusher_client = pusher.Pusher(
  app_id='1539110',
  key='e6cb6a190c13322ba2c2',
  secret='3c10f81db075cc839059',
  cluster='eu',
  ssl=True
)


@api_view(['GET', 'POST'])
def parking_list(request):

    # process:
    # get all the drink
    # serialize them
    # return json

    if request.method == 'GET':
        parkings = Parking.objects.all()
        serializer = ParkingSerializer(parkings, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ParkingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def parking_specific(request, id):
    try:
        parking = Parking.objects.get(pk=id)
    except Parking.DoesNotExist:
        return Response(status=status.HTTP_401_NOT_FOUND)
        
    if request.method == "GET":
        serializer = ParkingSerializer(parking)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = ParkingSerializer(parking, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method ==  "DELETE":
        parking.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# Paiement API

class PaiementAPI(generics.GenericAPIView):
    serializer_class = PaiementSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():

            serializer.save()
            pusher_client.trigger('my-channel', 'my-event', {'message': serializer.data.get('parking') })
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def paiement_list(request):
    
        # process:
        # get all the drink
        # serialize them
        # return json
    
        if request.method == 'GET':
            paiements = Paiement.objects.all()
            serializer = PaiementSerializer(paiements, many=True)
            return Response(serializer.data)
    
        if request.method == 'POST':
            serializer = PaiementSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                # pusher_client.trigger('my-channel', 'my-event', {'message': serializer.data.get('parking') })
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def paiement_specific(request, id):
    try:
        paiement = Paiement.objects.get(pk=id)
    except Paiement.DoesNotExist:
        return Response(status=status.HTTP_401_NOT_FOUND)
        
    if request.method == "GET":
        serializer = PaiementSerializer(paiement)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = PaiementSerializer(paiement, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method ==  "DELETE":
        paiement.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)