from django import forms

class IntegerDateForm(forms.Form):
    integer_value=forms.IntegerField()
    date_value=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
class PieChartForm(forms.Form):
    y_values = forms.CharField(label='Y Values', help_text='Enter comma-separated values')
    labels = forms.CharField(label='Labels', help_text='Enter comma-separated labels')