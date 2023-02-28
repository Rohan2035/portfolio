# Generated by Django 4.0.6 on 2022-09-23 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0014_alter_projects_technologies_used'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='git_hub_link',
            field=models.URLField(null=True, verbose_name='Git Hub Link'),
        ),
        migrations.AddField(
            model_name='projects',
            name='website_link',
            field=models.URLField(null=True, verbose_name='Website Link'),
        ),
    ]