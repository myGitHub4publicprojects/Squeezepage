from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^privacy_policy$', views.privacy_policy, name='privacy_policy'),
    # url(r'^register$', views.register, name='register'),
    url(r'^thank_you$', views.thank_you, name='thank_you'),
]