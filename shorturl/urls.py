from django.conf.urls.defaults import patterns, include, url
import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'shorturl.views.home', name='home'),
    url(r'^$', 'shorturl.views.home'),
    url(r'page/about/$', 'shorturl.views.about'),
    url(r'page/contact/$', 'shorturl.views.contact'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    
    url(r'^(?P<short>.+)/$', 'shorturl.views.short_url_redirect'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += patterns('',
)


