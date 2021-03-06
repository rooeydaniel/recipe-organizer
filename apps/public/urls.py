"""
This is your project's master URL configuration, it defines the set of "root" URLs for the entire project
"""
from django.conf.urls import patterns, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # These apply to the public app
    url(r'^login/$', TemplateView.as_view(template_name='login.html')),
    url(r'^$', TemplateView.as_view(template_name='home.html')),
)