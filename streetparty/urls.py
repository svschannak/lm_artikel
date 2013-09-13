from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from streetparty.views import StrassenFestList

urlpatterns = patterns('',
    # Examples:
    url(r'^', StrassenFestList.as_view(), name="feste"),


)
