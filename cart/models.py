from django.db import models

# Create your models here.
class CartItems(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    product_sku = models.ForeignKey('ProductSkus', models.DO_NOTHING)
    amount = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cart_items'