from decimal import Decimal
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit, Adjust

class Photo(models.Model):
    project = models.ForeignKey('Project')
    caption = models.CharField(max_length=150)
    position = models.PositiveSmallIntegerField(default=0)
    original = models.ImageField(upload_to='images')
    thumbnail = ImageSpecField([Adjust(contrast=1.2, sharpness=1.1),
            ResizeToFit(100, 100)], image_field='original',
            format='JPEG', options={'quality': 90})
    image = ImageSpecField([
            ResizeToFit(500, 500)], image_field='original',
            format='JPEG', options={'quality': 100})

class Project(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    budget = models.DecimalField(max_digits=20, decimal_places=2)
    total_fund = models.DecimalField(max_digits=20, decimal_places=2,
            default=Decimal('0.00'), editable=False)

    owner = models.ForeignKey('auth.User')

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    @property
    def progress(self):
        return (self.total_fund / self.budget) * 100

    @models.permalink
    def get_absolute_url(self):
        return ('proj:project_detail', (self.slug,))

