from user.models import Profile, Department, Town
from django.contrib.auth.hashers import make_password   
from rest_framework import serializers


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class TownSerializer(serializers.ModelSerializer):
    class Meta:
        model = Town
        fields = '__all__'
        depth = 1


class DoTownSerializer(serializers.ModelSerializer):
    class Meta:
        model = Town
        fields = '__all__'
        detph = 1


class ProfileSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        instance = Profile.objects.create_user(**validated_data)
        #instance.groups.add('Users')
        return instance
        
    class Meta:
        model = Profile
        fields = ('id', 'first_name', 'last_name', 'username',  'town', 'phone', 'email', 'password')


