"""
This is your project's master URL configuration, it defines the set of "root" URLs for the entire project
"""
from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('apps.authentication.views',
    # These apply to the public app
    # url(r'^$', 'get_user'),
    # url(r'^$', AuthUser.as_view(), name='auth_user')

    url(r'^logout/$', 'logout_view'),
    url(r'^loggedin/$', 'loggedin_view'),
    url(r'^invalid/$', 'invalid_login_view'),
    url(r'^$', 'authentication_view'),
)
