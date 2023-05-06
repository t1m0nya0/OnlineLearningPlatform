from rest_framework import serializers
from gratitudes.models import Gratitude


class GratitudeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    message = serializers.CharField(max_length=200)
    user = serializers.CharField(max_length=100)
    like_count = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        return Gratitude.objects.create(**validated_data)

    def update(self, instance, validated_data):
        print(instance.user)
        instance.message = validated_data.get('message', instance.message)
        instance.user = validated_data.get('user', instance.user)
        instance.save()
        return instance
