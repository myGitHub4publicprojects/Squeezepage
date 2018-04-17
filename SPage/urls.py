from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('collector.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.default.urls')),
]