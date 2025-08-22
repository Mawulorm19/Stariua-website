from django.db import models
from django.core.exceptions import ValidationError


def validate_pdf(value):
    if not value.name.endswith('.pdf'):
        raise ValidationError('Only PDF files are allowed.')


class HomepageBanner(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    background_video_url = models.URLField(blank=True, null=True)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)

    def __str__(self):
        return self.title







class AboutUs(models.Model):
    mission = models.TextField()
    vision = models.TextField()
    years_of_excellence = models.PositiveIntegerField(default=0)
    # Add any other fields you want admins to edit
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "About Us Content"

    


class StudentApplication(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    academic_results = models.FileField(upload_to='student_applications/', validators=[validate_pdf])

    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected')
    ], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class StaffAdmission(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    role_applied = models.CharField(max_length=100)  # e.g. "Math Teacher", "Clerk"
    application_letter = models.FileField(upload_to='staff_applications/', validators=[validate_pdf])
    cv = models.FileField(upload_to='staff_applications/', validators=[validate_pdf])

    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('accepted', 'Accepted'),
            ('rejected', 'Rejected')
        ],
        default='pending'
    )
    date_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
    
    

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class Staff(models.Model):
    TEACHING = 'Teaching'
    NON_TEACHING = 'Non-Teaching'

    ROLE_CHOICES = [
        (TEACHING, 'Teaching Staff'),
        (NON_TEACHING, 'Non-Teaching Staff'),
    ]

    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    position = models.CharField(max_length=100)
    qualifications = models.TextField(blank=True)
    photo = models.ImageField(upload_to='staff_photos/', blank=True, null=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname} - {self.position}"


class CampusTour(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='campus_tour/')
    is_visible = models.BooleanField(default=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


