

# Create your models here.
from django.db import models
from django import forms
from .models import Loan

class Loanform(forms.ModelForm):
    class Meta:
        model = Loan 
        fields = [ 'principle', 'tenure', 'interest', 'loan_type', 'name', 'address', 'phone_number', 'pan_number', 'aadhar_number', 'email']
        

    loan_type = forms.ChoiceField(
        widget= forms.RadioSelect,
        choices=[("1","Plan 1 Compound interest"), ("2","Plan 2 Simple interest")],
        initial = "1",
    )
