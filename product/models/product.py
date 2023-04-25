from django.db import models

from product.models.category import Category


class Product(models.Model):
    title = models.models.CharField(_("Title"), max_length=100)
    description = models.TextField(_("Description"), max_length=500, blank=True, null=False)
    price = models.PositiveIntegerField(_("Price"), null=True)
    active = models.BooleanField(default=True)
    categories = models.ManyToMany(Category, blank=True)
