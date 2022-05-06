from django import forms


class PeriodReportForm(forms.Form):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Start date")
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="End date")

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")
        if start_date > end_date:
            msg = 'The start date cannot be longer than the end date!'
            self.add_error('end_date', msg)
