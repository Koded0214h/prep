from django import forms

from .models import CustomUser, Provider, Patient

class RegisterForm(forms.ModelForm):
    
    password = forms.CharField(widget=forms.PasswordInput())
    c_password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = CustomUser
        fields = ['username','f_name','l_name','email','gender','role']
        
class ProviderForm(forms.ModelForm):
    
    class Meta:
        model = Provider
        fields = ['speciality','provider_dob']
        widgets ={
            'provider_dob': forms.DateInput(attrs={'type':'date'})
        }

class PatientForm(forms.ModelForm):
    
    class Meta:
        model = Patient
        fields = ['date_of_birth']
        widgets ={
            'provider_dob': forms.DateInput(attrs={'type':'date'})
        }