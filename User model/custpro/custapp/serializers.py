from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from custapp.models import Customer


class CustomerUserSerializers(serializers.ModelSerializer):
    # email = serializers.EmailField(max_length=255, required=True,
    #                                validators=[UniqueValidator(queryset=Customer.objects.all())])
    class Meta:
        model=Customer
        fields='__all__'

    def create(self, validated_data):
        print(validated_data)
        email = validated_data.pop('email')
        password = validated_data.pop('password')
        username = validated_data.pop('username')
        fisrtname = validated_data.pop('fisrtname')
        lastname = validated_data.pop('lastname')
        user = Customer.objects.create(email=email,username=username,fisrtname=fisrtname,lastname=lastname)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        print(validated_data)
        instance.email = validated_data.get('email',instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.username = validated_data.get('username', instance.username)
        instance.fisrtname = validated_data.get('fisrtname', instance.fisrtname)
        instance.lastname = validated_data.get('lastname', instance.lastname)
        instance.set_password(instance.password)
        instance.save()
        return instance




