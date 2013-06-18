from django.conf.urls import patterns, include, url
from vulnerableDjango import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'vulnerableDjango.views.home', name='home'),
    # url(r'^vulnerableDjango/', include('vulnerableDjango.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    ( r'^$', views.message ),
)
