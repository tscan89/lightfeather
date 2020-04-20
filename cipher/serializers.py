from rest_framework import serializers


class CipherSerializer(serializers.Serializer):
    shift = serializers.IntegerField()
    message = serializers.CharField()
