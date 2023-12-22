from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from loan_calculator.forms import Loanform
from loan_calculator.forms import ApplyLoanform
from django.http import HttpResponseRedirect  #v1
from django.shortcuts import render, get_object_or_404
from .models import Loan
from .models import ApplyLoan



# Create your views here.

class HomePageView(View):
    def get(self, request):
        return render(request, 'loan_calculator/home.html')
    
class LoanCalculatorView(View):
    def get(self, request):
        form = Loanform()
        return render(request, 'loan_calculator/calculate_loan.html', {'form': form})
    def post(self, request):
        form = Loanform(request.POST)
        if form.is_valid():
            loan = form.save(commit = False)     #not saving the data immediately
            if loan.loan_type =="1":
                loan.monthly_repayment = loan.principle / ((1 - (1 + loan.interest) ** (-loan.tenure)) / loan.interest) 
                #verify the formula
            elif loan.loan_type == "2":
                loan.monthly_repayment = (loan.principle + (loan.principle * loan.interest * loan.tenure)) / loan.tenure
                 #verify the formula
            else:
                return render(request, 'loan_calculator/error.html', {'loan': loan}) #should create this as pop-up for error
            loan.save()

            return HttpResponseRedirect(reverse('loan_calculator:results', args=[loan.id]))
            

class LoanResultsView(View):
    def get(self, request, loan_id):
        loan = get_object_or_404(Loan, id=loan_id)
        return render(request, 'loan_calculator/results.html', {'loan': loan})
    
class ApplyLoan(View):
    template_name = 'loan_calculator/applyloan.html'

    def get(self, request):
        loan = Loan.objects.last()
        form = ApplyLoanform()
        return render(request, self.template_name, {'form': form, 'loan':loan})

    def post(self, request):
        form = ApplyLoanform(request.POST)
        if form.is_valid():
            loan = form.save()
            return redirect('loan_calculator:success_page')
        else:
            return render(request, self.template_name, {'form': form})