from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__' # ['email', 'username', 'first_name', 'last_name', 'password']

        extra_kwards = {
            'password': {'write_only': True}
        }


class ApplicantSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Applicant
        fields = '__all__'
    
    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of applicant
        :return: returns a successfully created applicant record
        """
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        user.is_applicant = True
        applicant, created = Applicant.objects.update_or_create(user=user)
        return applicant


class RecruiterSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Recruiter
        fields = '__all__'
    
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        user.is_recruiter = True

        applicant, created = Recruiter.objects.update_or_create(user=user)
        return applicant
