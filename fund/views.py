import json
from django.views.generic import CreateView, TemplateView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from fund.forms import FundForm
from fund.models import Fund
from proj.models import Project
from django.shortcuts import get_object_or_404
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers

class FundFormView(CreateView):
    model = Fund
    template_name = 'fund/form.html'

    def get_form_class(self):
        return FundForm

    def form_valid(self, form):
        fund = form.save(commit=False)
        fund.funder = self.request.user
        fund.project = Project.objects.get(slug=self.kwargs['slug'])
        fund.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('proj:fund:success', kwargs=self.kwargs)

fund_form = FundFormView.as_view()

fund_success = TemplateView.as_view(template_name='fund/success.html')

def fund_data(request, slug):
    funds = Fund.objects.filter(project__slug=slug).all()
    json_serialized = serializers.serialize('json', funds)
    json_data = json.loads(json_serialized)
    return HttpResponse(json.dumps(json_data), content_type='application/json')
