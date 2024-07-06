import re
from django import forms
from signupApp.models import UserRegistration


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserRegistration
        fields ='__all__'
        # widgets => used to customize of fields in (rendering) but in database type that based on attributes in model
        genders=[{"male","Male"},{"female","Female"}] # (value,label)
        countries=[("select","Please Choose Country"), # (value,label)
                ("India","India"),
                ("Australia","Australia"),
                ("America","America"),
                ("Spain","Spain")
                ]
        
        widgets = {
                'password':forms.PasswordInput(),
                'confirmPassword':forms.PasswordInput(),
                'gender':forms.RadioSelect(choices=genders),
                'country':forms.Select(choices=countries),
                "birthDate":forms.DateInput(attrs={'type':'date'}),
                'email':forms.EmailInput(),
                'websiteUrl':forms.URLInput()
            }
        
    # validator to field (field level) must began with clean_nameoffiled using clean method
    def clean_phoneNumber(self):
        data = self.cleaned_data.get("phoneNumber")
        if data:
            pattern = re.compile(r'/^01[0125][0-9]{8}$/')
            if not re.fullmatch(pattern,data):
                raise forms.ValidationError("Invalid Phone Number Example: 01012352546")
            else:
                return data
        
    # validators to form (form level) using clean method 
    def clean(self): # when two fields related with eatch other in validation used clean method
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirmPassword = cleaned_data.get('confirmPassword')
        userName = cleaned_data.get('userName')
        country = cleaned_data.get('country')
        termsConditions = cleaned_data.get('termsConditions')
        
        if password and confirmPassword:
            if password != confirmPassword:
                raise forms.ValidationError("Passwords Don't Match")
   
        if userName and password:
            if userName == password:
                raise forms.ValidationError("UserName And Password Should be not same")
        
        if country == 'select':
            raise forms.ValidationError("Please Choose Country")
        
        if not termsConditions:
            raise forms.ValidationError("Please Agree to terms and conditions")
        
        return cleaned_data
              
        
        
    
    