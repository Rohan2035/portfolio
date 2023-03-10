# Generated by Django 4.0.6 on 2022-09-23 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0011_projects_alter_skills_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projects',
            options={'verbose_name_plural': 'Projects'},
        ),
        migrations.AddField(
            model_name='projects',
            name='about_project',
            field=models.TextField(null=True, verbose_name='About the Project'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='project_img',
            field=models.ImageField(upload_to='projects', verbose_name='Project Screenshot'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='project_name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
