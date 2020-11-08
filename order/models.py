from django.db import models
from user.models import Users
from product.models import Products,ProductSkus
# Create your models here.

class OrderItems(models.Model):
    order = models.ForeignKey('Orders', models.DO_NOTHING,verbose_name='所属订单 ID')
    product = models.ForeignKey('product.Products', models.DO_NOTHING,verbose_name='对应商品 ID')
    product_sku = models.ForeignKey('product.ProductSkus', models.DO_NOTHING,verbose_name='对应商品 SKU ID')
    amount = models.PositiveIntegerField(verbose_name='数量')
    price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='单价')
    rating = models.PositiveIntegerField(blank=True, null=True,verbose_name='用户打分')
    review = models.TextField(blank=True, null=True,verbose_name='用户评价')
    reviewed_at = models.DateTimeField(blank=True, null=True,verbose_name='评价时间')

    class Meta:
        db_table = 'order_items'
        # 模型在后台的名称
        verbose_name = "订单详情表"
        verbose_name_plural = verbose_name

class Orders(models.Model):
    no = models.CharField(unique=True, max_length=255,verbose_name='订单流水号')
    user = models.ForeignKey('user.Users', models.DO_NOTHING,verbose_name='下单的用户 ID')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='订单总金额')
    address = models.TextField(blank=True, null=True, verbose_name='收货地址')
    remark = models.TextField(blank=True, null=True,verbose_name='订单备注')
    paid_at = models.DateTimeField(blank=True, null=True,verbose_name='支付时间')
    payment_method = models.CharField(max_length=255, blank=True, null=True,verbose_name='支付方式')
    payment_no = models.CharField(max_length=255, blank=True, null=True,verbose_name='支付平台订单号')
    coupon_code_id = models.PositiveIntegerField(blank=True, null=True,verbose_name='')
    refund_status = models.CharField(max_length=255,verbose_name='退款状态')
    refund_no = models.CharField(unique=True, max_length=255, blank=True, null=True,verbose_name='退款单号')
    closed = models.IntegerField(blank=True, null=True,verbose_name='订单是否已关闭')
    reviewed = models.IntegerField(blank=True, null=True,verbose_name='订单是否已评价')
    extra = models.TextField(blank=True, null=True,verbose_name='其他额外的数据')
    created_at = models.DateTimeField(blank=True, null=True,verbose_name='创建时间')
    updated_at = models.DateTimeField(blank=True, null=True,verbose_name='更新时间')

    class Meta:
        db_table = 'orders'
        # 模型在后台的名称
        verbose_name = "订单表"
        verbose_name_plural = verbose_name

