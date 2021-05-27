from rest_framework import serializers
from testapp.models import ordertb

class orderSerializer(serializers.Serializer):
    oid = serializers.IntegerField()
    item = serializers.CharField(max_length=256)
    price = serializers.IntegerField()
    date = serializers.DateTimeField()


    def create(self, validated_data):
        return ordertb.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.oid=validated_data.get('oid',instance.oid)
        instance.item=validated_data.get('item',instance.item)
        instance.price=validated_data.get('price',instance.price)
        instance.date=validated_data.get('data',instance.date)
        instance.save()
        return instance

