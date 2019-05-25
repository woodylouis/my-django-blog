from customers.models import Customer
from customers.serializers import LeadSerializer
from rest_framework import generics
class LeadListCreate(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = LeadSerializer

