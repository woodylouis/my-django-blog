from rest_framework import serializers
from customers.models import Customer
class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'name', 'email', 'message')
