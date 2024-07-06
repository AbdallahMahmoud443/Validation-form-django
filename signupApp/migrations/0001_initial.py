# Generated by Django 5.0 on 2024-07-06 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=30, verbose_name='UserName')),
                ('password', models.CharField(max_length=30, verbose_name='Password')),
                ('confirmPassword', models.CharField(max_length=30, verbose_name='Confirm Password')),
                ('gender', models.CharField(max_length=10, verbose_name='Gender')),
                ('country', models.CharField(max_length=20, verbose_name='Country')),
                ('birthDate', models.DateField(verbose_name='Birth Date')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('postal', models.IntegerField(verbose_name='Postal Code')),
                ('phoneNumber', models.CharField(max_length=12, verbose_name='Phone Number')),
                ('profile', models.TextField(blank=True, max_length=500, verbose_name='Profile of User')),
                ('websiteUrl', models.URLField(verbose_name='Website URL')),
                ('termsConditions', models.BooleanField(verbose_name='Terms Condition')),
                ('favorWebsiteUrl', models.CharField(max_length=250)),
            ],
        ),
    ]
