# Generated by Django 4.0.6 on 2022-09-23 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0015_projects_git_hub_link_projects_website_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='project_name',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
