from django.db import models

# Create your models here.
class OrderItems(models.Model):
    order = models.ForeignKey('Orders', models.DO_NOTHING)
    product = models.ForeignKey('Products', models.DO_NOTHING)
    product_sku = models.ForeignKey('ProductSkus', models.DO_NOTHING)
    amount = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.PositiveIntegerField(blank=True, null=True)
    review = models.TextField(blank=True, null=True)
    reviewed_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_items'


class Orders(models.Model):
    no = models.CharField(unique=True, max_length=255)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    address = models.TextField(blank=True, null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    remark = models.TextField(blank=True, null=True)
    paid_at = models.DateTimeField(blank=True, null=True)
    coupon_code_id = models.PositiveIntegerField(blank=True, null=True)
    payment_method = models.CharField(max_length=255, blank=True, null=True)
    payment_no = models.CharField(max_length=255, blank=True, null=True)
    refund_status = models.CharField(max_length=255)
    refund_no = models.CharField(unique=True, max_length=255, blank=True, null=True)
    closed = models.IntegerField(blank=True, null=True)
    reviewed = models.IntegerField(blank=True, null=True)
    extra = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'

