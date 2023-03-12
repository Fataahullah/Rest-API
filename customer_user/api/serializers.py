from rest_framework import serializers
from api.models import User,Customer

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields="__all__"


class CustomerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model=Customer
        fields="__all__"
