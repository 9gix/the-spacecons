from django.conf.urls import patterns, include, url

urlpatterns = patterns('fund.views',
    url(r'^thanks/$', 'fund_success', name='success'),
    url(r'^data/$', 'fund_data', name='fund_data'),
    url(r'^$', 'fund_form', name='fund_form'),
)
