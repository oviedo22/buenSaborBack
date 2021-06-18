from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('pk','password', 'username', 'first_name', 'last_name','email','is_staff','fecha_nacimiento','imagen','telefono')