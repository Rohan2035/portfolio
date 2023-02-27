from django.shortcuts import render
from content.models import educationDetails, experienceDetails, skills
from content.models import projects
from math import ceil


# Project details function
def project_details(proj):

    tech_list = []

    for i in range(proj.count()):

        temp = str(proj[i].technologies_used).replace(" ", "")
        temp_list = temp.split(",")
        tech_list.append(temp_list)

    return tech_list 
        
# Index Page
def index(request):

    education_details = educationDetails.objects.all()
    experience_details = experienceDetails.objects.all()
    skill_details = skills.objects.all()
    proj = projects.objects.all()

    # Logic for Slides in Carousels
    no_of_slides = ceil(skill_details.count() / 3)

    # Logic for Technologies used in Projects
    tech_list = project_details(proj)

    context = {
        
        'educations' : education_details, 
        'experiences' : experience_details,
        'skills' : skill_details,
        'range' : range(1, no_of_slides),
        'projects' : proj,
        'tech_list' : tech_list 
    
    }


    return render(request, 'content/index.html', context)


# Contact Page
def contact(request):
    
    return render(request, 'content/contact.html')

