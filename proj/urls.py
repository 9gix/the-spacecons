from django.conf.urls import patterns, include, url

urlpatterns = patterns('proj.views',
    url(r'(?P<slug>[-\w]+)/fund/', include('fund.urls', namespace='fund')),
    url(r'(?P<slug>[-\w]+)', 'project_detail', name='project_detail'),
    url(r'^$', 'project_list', name='project_list'),
)
