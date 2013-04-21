from django.contrib import admin
from proj.models import Project
from proj.models import Photo

class PhotoInline(admin.StackedInline):
    model = Photo
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-open',)
    sortable_field_name = "position"
    sortable_excludes = ('caption', 'original')
    extra = 0


class ProjectAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]
    readonly_fields = ('total_fund',)
    date_hierarchy = 'created_at'
    list_display = ('name', 'description', 'budget', 'total_fund')
    list_filter = ('created_at', 'modified_at')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'description']

admin.site.register(Project, ProjectAdmin)
