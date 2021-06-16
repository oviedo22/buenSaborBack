from rest_framework import serializers
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = ('pk','nombre', 'apellido', 'dni', 'fecha_nacimiento','imagen','telefono')