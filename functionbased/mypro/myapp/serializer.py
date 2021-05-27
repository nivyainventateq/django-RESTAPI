from rest_framework import serializers
from myapp.models import Contactus



# class ContactusSerializer(serializers.Serializer):
#     name1=serializers.CharField(max_length=100)
#     phoneno = serializers.CharField(max_length=10)
#     place = serializers.CharField(max_length=100)
#     email = serializers.EmailField(max_length=100)
#
#
#     def create(self, validated_data):
#         return Contactus.object.create(validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name1=validated_data.get('name1',instance.name1)
#         instance.phoneno=validated_data.get('phoneno',instance.phoneno)
#         instance.place=validated_data.get('place',instance.place)
#         instance.email=validated_data.get('name1',instance.email)
#         instance.save()
#         return instance

class ContactusSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contactus
        fields = ('id','name1', 'phoneno','place','email')
