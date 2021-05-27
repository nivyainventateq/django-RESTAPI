from rest_framework import serializers
from myapp.models import Contactus


class ContactusSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contactus
        # fields=['id','name1','phoneno','place','email']
        fields='__all__'



