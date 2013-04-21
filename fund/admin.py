from django.contrib import admin
from fund.models import Fund

class FundAdmin(admin.ModelAdmin):
    model = Fund
    list_display = ('project', 'funder', 'amount',)

admin.site.register(Fund, FundAdmin)
