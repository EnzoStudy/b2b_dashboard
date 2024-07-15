from django import forms
from .models import Business,Performance

class PerformanceForm(forms.ModelForm):
    class Meta:
        model = Performance
        fields = ['name', 'participants', 'period_start', 'period_end', 'result']

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['name', 'expected_order_date', 'budget', 'sales_representative', 'sales_division','proposal_pm','is_strategic']


