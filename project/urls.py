from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from welcome.views import index, health, list_cases_json, list_cases,new_case

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index),
    url(r'^health$', health),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^list_cases_json/$$', list_cases_json),
    url(r'^list_cases/$$', list_cases),
    url(r'^new_case/$', new_case),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
