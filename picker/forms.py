from django import forms
from .models import Plan

class PlanForm(forms.ModelForm):

    class Meta:
        model = Plan
        fields =('title', 'description', 'price_point', 'location')

        def clean_field(self):
            data = self.cleaned_data['']
            if not data:
                data = 'default value'
            return data