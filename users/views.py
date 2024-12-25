from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view

from rest_framework import viewsets
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAdminUser,
    IsAuthenticated,
    AllowAny
)

from .models import *
from .serializers import *
from .permissions import *


 
class ApplicantViewSet(viewsets.ModelViewSet):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer
    

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = (IsOwnerOrReadOnly, )
        elif self.request.method == 'POST':
            self.permission_classes = (AllowAny,)
        elif self.request.method == 'PUT':
            self.permission_classes = (IsOwnerOrReadOnly, )
        elif self.request.method == 'DELETE':
            self.permission_classes = (IsAdminUser, )
        else: 
            self.permission_classes = (IsAuthenticatedOrReadOnly, )
        
        # return super().get_permissions()
        return super(ApplicantViewSet, self).get_permissions()

    
class RecruiterViewSet(viewsets.ModelViewSet):
    queryset = Recruiter.objects.all()
    serializer_class = RecruiterSerializer


