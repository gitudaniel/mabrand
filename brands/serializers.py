from django.contrib.auth.models import User

from rest_framework import serializers

from brands.models import Info


class InfoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    longitude = serializers.DecimalField(max_digits=9, decimal_places=6, coerce_to_string=False)
    latitude = serializers.DecimalField(max_digits=9, decimal_places=6, coerce_to_string=False)

    class Meta:
        model = Info
        exclude = ('longitude', 'latitude', 'owner')

    def create(self, validated_data):
        """
        Create and return a new `Info` instance, given the validated data.
        """
        return Info.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Info` instance, given the validated data.
        """
        instance.brand = validated_data.get('brand', instance.brand)
        instance.interviewee = validated_data.get('interviewee', instance.interviewee)
        instance.favorite = validated_data.get('favorite', instance.favorite)
        instance.disliked = validated_data.get('disliked', instance.disliked)
        instance.reason = validated_data.reason('reason', instance.reason)
        instance.longitude = validated_data.longitude('longitude', instance.longitude)
        instance.latitude = validated_data.get('latitude', instance.latitude)
        instance.save()
        return instance



class UserSerializer(serializers.ModelSerializer):
    info = serializers.PrimaryKeyRelatedField(many=True, queryset=Info.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'info')
