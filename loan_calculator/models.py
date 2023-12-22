from django.db import models

# Create your models here.
class Loan(models.Model):
    principle = models.FloatField()
    tenure = models.FloatField()
    interest = models.FloatField()
    loan_type = models.CharField(max_length=2, choices=[("1", "Plan 1 Compound intrest"),("2", "Plan2 Simple intrest")])
    monthly_repayment = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    name = models.CharField(max_length=32)
    address = models.TextField(max_length=100)
    phone_number = models.CharField(max_length=10)
    pan_number = models.CharField(max_length=10)
    aadhar_number = models.CharField(max_length=12)
    email = models.EmailField(null=True, blank=True)
