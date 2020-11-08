from django.db import models
from product.models import Products,ProductSkus
from user.models import Users
# Create your models here.

# 购物车
class CartItems(models.Model):
    product_sku = models.ForeignKey('product.ProductSkus', models.DO_NOTHING, verbose_name='商品SKU ID')
    user = models.ForeignKey('user.Users', models.DO_NOTHING,verbose_name='用户ID')
    amount = models.PositiveIntegerField()

    class Meta:
        db_table = 'cart_items'
        # 模型在后台的名称
        verbose_name = "购物车"
        verbose_name_plural = verbose_name