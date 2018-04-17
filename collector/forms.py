from django import forms
from .models import SignUp

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name', 'email']
        labels = {'email': 'Your email'}

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        if 'a' not in full_name:
            raise forms.ValidationError("Please use a name with an 'a' in it!")
        return full_name