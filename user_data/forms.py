from django import forms
from django.contrib.auth.forms import UserCreationForm    # step 1
from django.contrib.auth.models import User

class NewReg(UserCreationForm):
    # email = forms.EmailField()  # if we want to conmplsory then only 
    # first_name = forms.CharField()
    # last_name = forms.CharField()
    class Meta:
        model = User
        fields = ("username",'first_name',"last_name","email")
        def save(self, commit=True):
            user = super(NewReg,self).save(commit=False)
            user.email = self.cleaned_data['email']
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.is_staff = True
            if commit:
                user.save()
            return user
        
# class LogForm(forms.Form):
#     username = forms.CharField(widget=forms.TextInput())
#     password = forms.CharField(widget=forms.PasswordInput())

