from django.forms import model_to_dict
from rest_framework import generics, viewsets, mixins
from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated


from .models import Education, Job
from .permissions import *
from .serializers import EducationSerializer, JobSerializer


from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Education, Applicant
from .serializers import EducationSerializer, ApplicantSerializer


# EDUCATION

class EducationAPIList(generics.ListCreateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = (IsApplicant, )

    def post(self, request, *args, **kwargs):
        education_data = request.data.copy()  # Make a mutable copy of the data
        
        # Use the logged-in user's information
        user = request.user
        if not user.is_authenticated:
            return Response({'error': 'User is not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
        
        if user.is_applicant:
            education_data['user'] = user.id
            education_serializer = EducationSerializer(data=education_data)
            if education_serializer.is_valid():
                education_serializer.save()
                return Response(education_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(education_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'User is not an applicant'}, status=status.HTTP_401_UNAUTHORIZED)
        # # Assign the user instance to the education data
        # education_data['user'] = user.id
        
        # # Deserialize education data
        # education_serializer = EducationSerializer(data=education_data)
        # if education_serializer.is_valid():
        #     education_serializer.save()
        #     return Response(education_serializer.data, status=status.HTTP_201_CREATED)
        # else:
        #     return Response(education_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EducationAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    # permission_classes = (IsAuthenticated, )
    # authentication_classes = (TokenAuthentication, )


class EducationAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    # permission_classes = (IsAdminOrReadOnly, )


# JOB

class JobAPIList(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = (IsAdminUser, )


class JobAPICreate(generics.CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class JobAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    # permission_classes = (IsAuthenticated, )
    # authentication_classes = (TokenAuthentication, )


class JobAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = (IsAdminOrReadOnly, )