from django.db import models
from django.db.models.signals import post_save
from django.db.models.aggregates import Sum

class Fund(models.Model):
    project = models.ForeignKey('proj.Project')
    funder = models.ForeignKey('auth.User')
    amount = models.DecimalField(max_digits=20, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "Project: %s has received $%s from %s" % (
                self.project, self.amount, self.funder)

    def get_project_total_fund(self):
        fund = Fund.objects.filter(project=self.project).aggregate(Sum('amount'))
        return fund['amount__sum']



def update_project_total_fund(sender, instance, **kwargs):
    from proj.models import Project
    Project.objects.filter(pk=instance.project.pk).update(
            total_fund=instance.get_project_total_fund())

post_save.connect(update_project_total_fund, Fund)
