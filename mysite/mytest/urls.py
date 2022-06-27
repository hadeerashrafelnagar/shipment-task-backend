from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

router.register(r'shipment', ShipmentViewSet)
router.register(r'journal', JournalViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('getShipmentDetails/', GetShipmentDetails.as_view()),
    path('addShipment/', AddShipment.as_view()),
    path('shipment/<int:id>', DeleteShipment.as_view()),
    path('changeShipmentStatus/', ChangeShipmentStatus.as_view() ),
    path('addJournal/', AddJournal.as_view()),
    path('journal/', GetJournalDetails.as_view()),
]
