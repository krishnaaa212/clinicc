from django import forms
from .models import *

class AppointmentForm(forms.ModelForm):
    class Meta :
        model=Appointments
        fields = '__all__'