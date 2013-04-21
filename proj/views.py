from django.views.generic import DetailView, ListView
from chartit import DataPool, Chart
from proj.models import Project


class ProjectDetailView(DetailView):
    model = Project

class ProjectListView(ListView):
    model = Project

project_detail = ProjectDetailView.as_view()
project_list = ProjectListView.as_view()
