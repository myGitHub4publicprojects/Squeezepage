from django import forms

from .models import SignUp

class SignUpForm(forms.ModelForm):
    full_name = forms.CharField(max_length=120, label='Full name')
    email = forms.EmailField(label='Your email')
    class Meta:
        model = SignUp
        fields = ['full_name', 'email']




    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     email_base, provider = email.split("@")
    #     domain, extension = provider.split('.')
	# 	# if not domain == 'USC':
	# 	# 	raise forms.ValidationError("Please make sure you use your USC email.")
    #     if not extension == "edu":
    #         raise forms.ValidationError("Please use a valid .EDU email address")
    #     return email
    # def clean_full_name(self):
    #     full_name = self.cleaned_data.get('full_name')
    #     if 'a' not in full_name:
    #         raise forms.ValidationError("Please use a name with an 'a' in it!")
    #     return full_name