from django.conf.urls.defaults import *

from django.contrib import admin
import settings

handler500 = 'Polls.views.page_not_found'
handler404 = 'Polls.views.page_not_found'
admin.autodiscover()

urlpatterns = patterns('',
    (r'^media/(.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    (r'^enquete/', include('Photopolls.Polls.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^facebook/', include('django_facebook.urls')),
    #(r'^accounts/', include('django_facebook.auth_urls')),
    #url(r'^admin/', include(admin.site.urls)),
)
