from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'studbook.views.home_page', name='home'),
    url(r'^new$', 'studbook.views.new', name='new')
)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
