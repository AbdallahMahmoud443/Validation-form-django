from django.shortcuts import render

from signupApp.forms import UserRegistrationForm

# Create your views here.




def SignUpView(request):
    pagePath = 'signupApp/signupPage.html'
    if request.method =="POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid: # this statement is important for validation work 
            #form.save()
            return render(request,pagePath,{'form':form})
    else:
        form = UserRegistrationForm() 
        
    return render(request,pagePath,{'form':form})