from django import forms
from fund.models import Fund

class FundForm(forms.ModelForm):
    class Meta:
        model = Fund
        fields = ('amount',)

    def save(self, force_insert=False, force_update=False, commit=True):
        m = super(FundForm, self).save(commit=False)
        if commit:
            m.save()
        return m
