import os
from django.conf.urls import patterns, include, url
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.dates import DateDetailView, YearArchiveView, MonthArchiveView, DayArchiveView
from django.conf import settings

from django.contrib import admin

import settings


admin.autodiscover()


urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),
    url(r'^admin/', include(admin.site.urls)),
)
