from django import forms
from .models import emp
class Date(forms.DateInput):
    input_type = "date"

# class UpdateForm(forms.Form):
#     name = forms.CharField(widget=forms.TextInput())
#     joining_date = forms.DateField(widget=Date())
#     email_id = forms.EmailField(widget=forms.EmailInput())
#     department = forms.CharField(widget=forms.TextInput())
#     salary = forms.FloatField(widget=forms.NumberInput())
#     job_status = forms.CharField(widget=forms.TextInput)
#     is_active = forms.BooleanField(widget=forms.CheckboxInput())
#     created_by = forms.c

class UpdateForm(forms.ModelForm):
    joining_date = forms.DateField(widget=Date())
    class Meta:
        model = emp
        exclude = ['created_by']




