from rest_framework import serializers
from taskapp.models import User


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

    def create(self, validated_data):
        print(validated_data)
        email = validated_data.pop('email')
        password = validated_data.pop('password')
        username = validated_data.pop('username')
        user = User.objects.create(email=email,username=username)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        print(validated_data)
        instance.email = validated_data.get('email',instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.username = validated_data.get('username', instance.username)
        instance.save()
        return instance


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=256, required=True)
    password = serializers.CharField(required=True, min_length=5)

    class Meta:
        model = User



