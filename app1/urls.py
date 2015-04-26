from django.conf.urls import patterns, url
from app1 import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'form_manytomany.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^article/(?P<id>\d+)/$', views.article, name='article_detail'),
    url(r'^article/(?P<id>\d+)/comment/$', views.article, name='article_comment'),
)
