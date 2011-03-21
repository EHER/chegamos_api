from django.conf.urls.defaults import *
from piston.resource import Resource
from chegamos_api.api.handlers import *

badge_resource = Resource(BadgeHandle)
rule_resource = Resource(RuleHandle)
history_resource = Resource(HistoryHandle)

urlpatterns = patterns('',
    url(r'^badges/(?P<id>\d+)$', badge_resource),
    url(r'^badges$', badge_resource),
    url(r'^rule/(?P<id>\d+)$', rule_resource),
    url(r'^rule$', rule_resource),
    url(r'^history/(?P<id>\d+)$', history_resource),
    url(r'^history$', history_resource),
)


