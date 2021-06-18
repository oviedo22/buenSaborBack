from rest_framework import serializers
from .models import User,Domicilio

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('pk','password', 'username', 'first_name', 'last_name','email','is_staff','fecha_nacimiento','imagen','telefono')

class DomicilioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Domicilio
        fields = ('pk','calle','numero','localidad')