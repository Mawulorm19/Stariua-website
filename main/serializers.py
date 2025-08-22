from rest_framework import serializers
from .models import AboutUs


from .models import AboutUs

class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'


from .models import StudentApplication, StaffAdmission , Event

class StudentApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentApplication
        fields = '__all__'
        

class StaffAdmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffAdmission
        fields = '__all__'



class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        
        
        
from .models import Staff

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'


from .models import CampusTour

class CampusTourSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampusTour
        fields = '__all__'
