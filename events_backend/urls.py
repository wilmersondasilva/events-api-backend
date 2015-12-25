from django.conf.urls import include, url
from django.contrib import admin

from events import urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^events/api/', include(urls)),
]
