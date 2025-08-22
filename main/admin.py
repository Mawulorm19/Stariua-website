from django.contrib import admin
from django.utils.html import format_html
from .models import CampusTour


from .models import AboutUs

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('years_of_excellence', 'updated_at')

    
    

from .models import StudentApplication

@admin.register(StudentApplication)
class StudentApplicationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'status', 'created_at', 'view_academic_results')
    list_filter = ('status',)
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    
    
    def view_academic_results(self, obj):
        if obj.academic_results:
            return format_html(
                '<a href="{}" target="_blank">View PDF</a>',
                obj.academic_results.url
            )
        return "No file uploaded"
    view_academic_results.short_description = "Academic Results"
    
    
   
    
   


from .models import StaffAdmission

@admin.register(StaffAdmission)
class StaffAdmissionAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'phone', 'role_applied', 'status')
    list_filter = ('status',)
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    
    
    
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'time', 'location', 'is_published')
    list_filter = ('date', 'is_published')
    search_fields = ('title', 'description', 'location')



from .models import Staff

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'position', 'role', 'is_visible')
    list_filter = ('role', 'is_visible')
    search_fields = ('firstname', 'lastname', 'position')
    
    
from .models import CampusTour

@admin.register(CampusTour)
class CampusTourAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_visible', 'uploaded_at']
    list_filter = ['is_visible']
    search_fields = ['title']


admin.site.site_header = 'Stariua Administration'
admin.site.site_title = 'Stariua Administration Portal'
admin.site.index_title = 'Welcome to Stariua Administration'