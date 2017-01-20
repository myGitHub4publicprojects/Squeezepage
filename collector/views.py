from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import SignUpForm
from django.core.mail import send_mail
from django.conf import settings
from .models import SignUp

def home(request):
    form = SignUpForm(request.POST or None)
    context = {
        'form': form
        }
    
    if form.is_valid():
        email = form.cleaned_data.get("email")
        full_name = form.cleaned_data.get("full_name")
        form.save()
        send_mail(
            'Thank you for your interest',
            'Dear %s,\nhere is the link to our training program:\nhttp:someurl \nKind Regards XYZ Team'%full_name,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
            )
        return HttpResponseRedirect('thank_you')
    
    if request.user.is_staff:
        queryset = SignUp.objects.all()
        context = {'queryset': queryset}

    return render(request, 'collector/home.html', context)

def privacy_policy(request):
    return render(request, 'collector/privacy_policy.html', {})

def thank_you(request):
    return render(request, 'collector/thank_you.html', {})
    