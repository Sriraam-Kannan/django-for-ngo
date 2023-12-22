"""
URL configuration for NGO project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from loan_calculator.views import HomePageView, LoanCalculatorView , ApplyLoan


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('loan_calculator/', include(('loan_calculator.urls', 'loan_calculator'), namespace='loan_calculator')),
    path('apply_loan/', include(('apply_loan.urls', 'apply_loan'), namespace='apply_loan')),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)