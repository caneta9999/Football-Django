from django import forms
from .models import Team

class CreateNewMessage(forms.Form):
    name = forms.CharField(label='Name', max_length=80)
    message = forms.CharField(max_length=500, widget=forms.Textarea(attrs={"rows":"5"}))
    favTeam = forms.ModelChoiceField(queryset=Team.objects.filter().order_by('name'))