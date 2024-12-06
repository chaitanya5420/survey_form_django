# Generated by Django 5.1.4 on 2024-12-06 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey_app', '0004_alter_surveyresponse_blood_donation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyresponse',
            name='blood_donation',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='surveyresponse',
            name='covid_vaccination',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3),
        ),
        migrations.AlterField(
            model_name='surveyresponse',
            name='dairy_consumption',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='surveyresponse',
            name='hair_loss',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='surveyresponse',
            name='vision_problems',
            field=models.BooleanField(default=False),
        ),
    ]
