from django.contrib import admin
from content.models import educationDetails, experienceDetails, skills, projects

# Register your models here.
admin.site.register(educationDetails)
admin.site.register(experienceDetails)
admin.site.register(skills)
admin.site.register(projects)