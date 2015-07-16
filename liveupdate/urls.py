from django.views.generic.list import ListView
from django.conf.urls import patterns, url
from liveupdate.models import Update
from liveupdate.views import update_after

urlpatterns = patterns('django.views.generic',
                       url(r'^$', ListView.as_view(model=Update,), {
                           'queryset': Update.objects.all()
                       }),
                       url(r'^updates-after/(?P<id>\d+)/$', update_after),
)