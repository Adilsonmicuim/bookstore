from django.db import models


class Category(models.Model):
    title = models.CharField(_("Title"), max_length=100)
    slug = models.SlugField(_("Slug"), unique=True)
    description = models.CharField(_("Description"), max_length=200, blank=True, null=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title
