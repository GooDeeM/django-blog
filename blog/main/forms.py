from django import forms

from .models import BlogUser

class ChangeUserInfoForm(forms.ModelForm):
    email = forms.EmailField(required=True, label='адреса електронної пошти')
    class Meta:
        model = BlogUser
        fields = ('username', 'email', 'first_name', 'last_name')
