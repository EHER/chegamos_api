from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^chegamos_api/', include('chegamos_api.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^badges/$', 'badges.views.index'),
    (r'^badges/(?P<badge_id>\d+)/$', 'badges.views.detail'),
    # Uncomment the next line to enable the admin:
    (r'^api/', include('chegamos_api.api.urls')),
    (r'^admin/', include(admin.site.urls)),
)
