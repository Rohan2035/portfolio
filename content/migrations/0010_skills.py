# Generated by Django 4.0.6 on 2022-08-21 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0009_alter_educationdetails_card_color_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=50, null=True, verbose_name='Skill Name')),
                ('image_skill', models.ImageField(null=True, upload_to='skills')),
            ],
        ),
    ]
