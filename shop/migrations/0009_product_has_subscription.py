# Generated by Django 3.2.9 on 2021-12-16 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_remove_product_stripe_subscription_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='has_subscription',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]