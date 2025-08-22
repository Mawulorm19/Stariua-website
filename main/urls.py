from django.urls import path
from . import views
from .views import AboutUsAPIView


from .views import StudentApplicationAPIView, StaffAdmissionAPIView
#from .views import EventListCreateAPIView, EventDetailAPIView
#from .views import StaffListAPIView
#from .views import CampusTourListAPIView
from .views import CampusTourCreateAPIView


urlpatterns = [
    path('', views.homepage, name='homepage'),
    
    
     path('api/about-us/', AboutUsAPIView.as_view(), name='about-us-api'),
     

    
    path('api/student-application/', StudentApplicationAPIView.as_view(), name='student_application'),
     
    path('api/staff-admission/', StaffAdmissionAPIView.as_view(), name='staff_admission'),
     
    #path('events/', EventListCreateAPIView.as_view(), name='event-list-create'),
     
    #path('events/<int:id>/', EventDetailAPIView.as_view(), name='event-detail'),
    
    #path('api/staff/', StaffListAPIView.as_view(), name='staff-list'),
    
    #path('api/campus-tour/', CampusTourListAPIView.as_view(), name='campus-tour'),
    
     path('api/campus-tour/upload/', CampusTourCreateAPIView.as_view(), name='campus-tour-upload'),
]

