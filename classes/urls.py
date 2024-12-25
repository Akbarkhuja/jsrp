from django.urls import path, include
from rest_framework import routers

from .views import *


urlpatterns = [
    path('education/', EducationAPIList.as_view()),
    path('education/<int:pk>/', EducationAPIUpdate.as_view()),
    path('education/<int:pk>/', EducationAPIDestroy.as_view()),

    path('job/', JobAPIList.as_view()),
    path('job/<int:pk>/', JobAPIUpdate.as_view()),
    path('job/<int:pk>/', JobAPIDestroy.as_view()),
    path('job/create/', JobAPICreate.as_view()),
]