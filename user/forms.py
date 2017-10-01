from .models import User
from django import forms

class RegistrationRequest(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "starting_year"]

class ApproveRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ["is_awaiting_approval"]
