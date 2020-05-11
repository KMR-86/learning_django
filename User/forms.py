from django import forms
from .models import User

class user_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ["name", "profile_bio", "profile_picture", "total_friends"]
