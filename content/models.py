from django.db import models

# Card colors
choices = [('b-success', 'Green'), ('b-danger', 'Red'), ('b-warning', 'Yellow'), ('b-info', 'Light Blue')] 

class educationDetails(models.Model):

    class Meta:

        verbose_name_plural = "Education Details"

   

    institution_name = models.CharField(max_length=50, null=True, verbose_name="Institution Name")
    course_studied = models.CharField(max_length=50, null=True, verbose_name="Course Studied")
    year_of_joining = models.CharField(max_length=50 ,verbose_name="From", null=True)
    year_of_leaving = models.CharField(max_length=50 ,verbose_name="To", null=True)
    card_color = models.CharField(max_length=50, verbose_name='Flashcard Color', choices=choices, null=True)


    def __str__(self):

        return self.institution_name

class experienceDetails(models.Model):

    class Meta:

        verbose_name_plural = "Experience Details"
        

    company_name = models.CharField(max_length=50, null=True, verbose_name="Company Name")
    position = models.CharField(max_length=50, verbose_name="Position", null="True")
    year_of_joining = models.CharField(max_length=50 ,verbose_name="From", null=True)
    year_of_leaving = models.CharField(max_length=50 ,verbose_name="To", null=True)
    card_color = models.CharField(max_length=50, verbose_name='Flashcard Color', choices=choices, null=True)

    def __str__(self):

        return self.company_name

class skills(models.Model):

    class Meta:

        verbose_name_plural = "Skills"

    
    skill_name = models.CharField(max_length = 50, null=True, verbose_name='Skill Name')
    image_skill = models.ImageField(null=True, upload_to='skills')

    def __str__(self):

        return self.skill_name

class projects(models.Model):

    class Meta:

        verbose_name_plural = "Projects"

    project_id = models.AutoField(primary_key = True)
    project_name = models.CharField(max_length = 300, null=True)
    about_project = models.TextField(null=True, verbose_name="About the Project")
    technologies_used = models.TextField(null=True, verbose_name="Technologies Used (Use comma to separate the words)")
    
    project_img = models.ImageField(upload_to="projects", verbose_name="Project Screenshot")
    git_hub_link = models.URLField(max_length=200, verbose_name="Git Hub Link", null=True, blank=True)
    website_link = models.URLField(max_length=200, verbose_name="Website Link", null = True, blank=True)

    def __str__(self):

        return self.project_name