from rest_framework import serializers
from .models import *

# shipment serializer

class ShipmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shipment
        fields = ('id','code', 'name', 'weight', 'description', 'status','price','time','date')

# journal serializer

class JournalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Journal
        fields = ('id','type','amount','shipment')
        
