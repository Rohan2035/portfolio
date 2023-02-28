# Generated by Django 4.0.6 on 2022-08-10 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_educationdetails_card_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiencedetails',
            name='card_color',
            field=models.CharField(choices=[('1', 'b-success'), ('2', 'b-danger'), ('3', 'b-warning'), ('4', 'b-info')], max_length=50, null=True, verbose_name='Flashcard Color'),
        ),
    ]