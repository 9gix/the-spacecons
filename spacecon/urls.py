from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

class HomeView(TemplateView):
    template_name = 'index.html'

home = HomeView.as_view()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^project/', include('proj.urls', namespace='proj')),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^$', home, name='home'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
