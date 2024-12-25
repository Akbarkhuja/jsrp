from rest_framework import serializers

from .models import Education, Job
from users.serializers import *


class EducationSerializer(serializers.ModelSerializer):
    # applicant = serializers.HiddenField(default=ApplicantSerializer())
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Education
        fields = '__all__'


class JobSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Job
        fields = '__all__'