from django.conf.urls import patterns, include, url

from django.contrib import admin
import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'QRDecoder.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^decode/(?P<base_64>.+)/$',views.makeData),
    url(r'^$',views.index),
    url(r'^admin/', include(admin.site.urls)),
)
