from rest_framework import viewsets
from .models import Journal, Shipment
from .serializers import JournalSerializer, ShipmentSerializer
from rest_auth.views import APIView 
import json
from django.http import JsonResponse
from django.core import serializers
from django.views.generic.detail import DetailView


# Create your views here.

# shipment view
class ShipmentViewSet(viewsets.ModelViewSet):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer



# journal view
class JournalViewSet(viewsets.ModelViewSet):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer


# get all shipments details function
class GetShipmentDetails(APIView):

    def get(self, request, *args, **kwargs):
        try:
            details = serializers.serialize("json", Shipment.objects.all().order_by('-createdOn'))
            jsonDetails = json.loads(details)
            return JsonResponse({'result': jsonDetails}, status=200)
        except:
            return JsonResponse({'result': 'something went wrong'}, status=200)



# add new shipment function
class AddShipment(APIView):

    def post(self, request, *args, **kwargs):

        orderName = request.data['name']
        orderWeight = request.data['weight']
        orderdescription = request.data['description']
        try:
            newShipment = Shipment(name=orderName, weight=orderWeight,
                                   description=orderdescription)
            newShipment.save()
            return JsonResponse({"result": "your shipment placed successfully"}, status=200)
        except:
            return JsonResponse({'result': "something went wrong"}, status=200)



# change shipments status(progress/pending/done) function
class ChangeShipmentStatus(APIView):

    def put(self, request, *args, **kwargs):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        id = body['id']
        editedstatus = body['editedstatus']
        try:
            shipment = Shipment.objects.get(id=id)
            shipment.status = editedstatus
            shipment.save()
            return JsonResponse({'result': 'Shipment is updated successfully'}, status=200)
        except:
            return JsonResponse({'result': "something went wrong"}, status=200)
    



# delete shipment function        
class DeleteShipment(DetailView):

    def delete(self, request, *args, **kwargs):
        try:
            orderId = request.data['id']
            order = Shipment.objects.filter(id=orderId)
            order.delete()
            return JsonResponse({'result': 'shipment has deleted suceesfully'}, status=200)
        except:
            return JsonResponse({'result': "shipment hasn't deleted suceesfully"}, status=200)




# add new journal for specific shipment function        
class AddJournal(APIView):
    def post(self, request, *args, **kwargs):
        try:
            shipmentId = request.data['id']
            journalType= request.data['type']
            orderShipment = Shipment.objects.get(id=shipmentId)
            if (journalType=="debitCash"):
                amount=orderShipment.price
            elif(journalType=="creditRevenue"):
                amount=orderShipment.price * 20/100
            elif(journalType=="creditPayable"):
                amount=orderShipment.price * 80/100
            newJournal = Journal(shipment=orderShipment,type=journalType,amount=amount)
            newJournal.save()
            return JsonResponse({"result": "Journals added successfully"}, status=200)
        except:
            return JsonResponse({'result': "something went wrong"}, status=200)



# get journal details for specific shipment function        
class GetJournalDetails(APIView):

    def get(self, request, *args, **kwargs):
        try:
            details = serializers.serialize("json", Journal.objects.all())
            jsonDetails = json.loads(details)
            return JsonResponse({'result': jsonDetails}, status=200)
        except:
            return JsonResponse({'result': 'something went wrong'}, status=200)
