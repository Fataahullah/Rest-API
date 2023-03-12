from django.shortcuts import render
from rest_framework import viewsets
from api.serializers import UserSerializer,CustomerSerializer
from api.models import User,Customer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer
