"""
This is your project's master URL configuration, it defines the set of "root" URLs for the entire project
"""
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^project/', include('project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Static files, served from server
    #url(r'^static/(\?P.*)$', 'django.views.static.serve', {'document_root': base.STATIC_ROOT}),

    url(r'^authentication/', include('apps.authentication.urls')),
    url(r'^recipe/', include('apps.recipe.urls')),
    url(r'^', include('apps.public.urls')),
)
