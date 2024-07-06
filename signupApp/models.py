import re
from django.db import models
from django.core.validators import MinLengthValidator,MinValueValidator,MaxValueValidator
from django.core.exceptions import ValidationError
# Create your models here.

class UserRegistration(models.Model):
    
    #Custom Validators
    def validate_favorWebsiteUrl(iUrl): # best 
        pattern = re.compile(r"^https\://[a-zA-Z0-9\-\.]+\.[a-zA-Z]{2,3}(/\S*)?$")
        if not re.fullmatch(pattern,iUrl):
            raise ValidationError('Invalid URL Example:https://www.google.com')
        
    # Built-in validators functions using django 
    userName = models.CharField(max_length=30,
                                verbose_name="UserName",
                                validators=[MinLengthValidator(5,message="Please Enter Character Greater than 5")]) # custom message in bulit in validator
    
    password = models.CharField(max_length=30,
                                verbose_name="Password",
                                validators=[MinLengthValidator(5)])
    
    confirmPassword = models.CharField(max_length=30,
                                       verbose_name="Confirm Password",
                                       validators=[MinLengthValidator(5)])
    
    gender = models.CharField(max_length=10,
                              verbose_name="Gender")
    
    country = models.CharField(max_length=20,
                               verbose_name="Country")
    
    birthDate = models.DateField(verbose_name="Birth Date")
    email = models.EmailField(verbose_name="Email")
    
    postal = models.IntegerField(verbose_name="Postal Code",
                                validators=[MinValueValidator(1000),
                                            MaxValueValidator(10000)])
    
    phoneNumber = models.CharField(max_length=12,
                                   verbose_name="Phone Number")
    
    profile = models.TextField(max_length=500,
                               verbose_name="Profile of User",
                               blank=True) # blank=True => Optional field
    
    websiteUrl = models.URLField(verbose_name="Website URL")
    termsConditions = models.BooleanField(verbose_name="Terms Condition") # BooleanField => CheckBox
    favorWebsiteUrl = models.CharField(max_length=250,validators=[validate_favorWebsiteUrl]) # validate_favorWebsiteUrl => custom validator
    