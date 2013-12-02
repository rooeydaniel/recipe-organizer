"""
This is your project's master URL configuration, it defines the set of "root" URLs for the entire project
"""
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from settings import base

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	# These apply to the public app
	url(r'^angular-test[/]$', TemplateView.as_view(template_name='angular-test.html')),
	url(r'^$', TemplateView.as_view(template_name='home.html')),
)
