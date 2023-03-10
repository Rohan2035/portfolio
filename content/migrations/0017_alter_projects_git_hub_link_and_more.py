# Generated by Django 4.0.6 on 2022-09-23 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0016_alter_projects_project_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='git_hub_link',
            field=models.URLField(blank=True, null=True, verbose_name='Git Hub Link'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='website_link',
            field=models.URLField(blank=True, null=True, verbose_name='Website Link'),
        ),
    ]
