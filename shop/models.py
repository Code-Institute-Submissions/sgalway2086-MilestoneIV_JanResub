from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    has_subscription = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    review_quantity = models.DecimalField(default=0, max_digits=10, decimal_places=0)


    def __str__(self):
        return self.name


class Subscription(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    customer_id = models.CharField(max_length=255)
    subscription_id = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username


class Review(models.Model):
    user = models.CharField(max_length=254, null=False, blank=False)
    title = models.CharField(default='', max_length=254)
    review_for_product_id = models.DecimalField(default=0, max_digits=10, decimal_places=0)
    rating = models.DecimalField(max_digits=1, decimal_places=0, null=True, blank=True)
    review_text = models.TextField()
