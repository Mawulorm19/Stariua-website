from django.shortcuts import render
from django.http import JsonResponse


def homepage(request):
    return JsonResponse({"message": "Welcome to Stariua Preparatory School"})



from rest_framework.views import APIView
from rest_framework.response import Response
from .models import AboutUs
from .serializers import AboutUsSerializer

class AboutUsAPIView(APIView):
    def get(self, request):
        about = AboutUs.objects.first()  # Assuming only one AboutUs entry
        serializer = AboutUsSerializer(about)
        return Response(serializer.data)
    
    





from .models import StudentApplication
from .serializers import StudentApplicationSerializer, StaffAdmissionSerializer





from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class StudentApplicationAPIView(APIView):
    def post(self, request):
        serializer = StudentApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Student application submitted successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StaffAdmissionAPIView(APIView):
    def post(self, request):
        serializer = StaffAdmissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Staff application submitted successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    




 


from .models import CampusTour
from .serializers import CampusTourSerializer


from rest_framework.permissions import IsAdminUser
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.generics import CreateAPIView

class CampusTourCreateAPIView(CreateAPIView):
    queryset = CampusTour.objects.all()
    serializer_class = CampusTourSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAdminUser]
