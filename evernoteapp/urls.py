from django.conf.urls.defaults import patterns, include, url
from settings import MEDIA_ROOT
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url('^$', 'account.views.home_page'),
    url(r'^login/$', 'account.views.login_page' ),
    url('^home/$', 'basic.views.landing'),
    url('^post_token/$', 'basic.views.post_evernote_token'),
    url('^auth/gettok/$', 'basic.views.run_evernote_auth'),
    url('^auth/usertok/$', 'basic.views.get_evernote_token'),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': MEDIA_ROOT}),
    url(r'^account/', include('account.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
