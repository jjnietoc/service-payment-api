from rest_framework import serializers
from pagos.models import Pagos, Services, PaymentUser, ExpiredPayments

class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagos
        fields = '__all__'
        read_only_fields = '__all__',

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'
        read_only_fields = '__all__',

class PaymentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentUser
        fields = '__all__'
        read_only_fields = '__all__',

class ExpiredPaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpiredPayments
        fields = '__all__'
        read_only_fields = '__all__'