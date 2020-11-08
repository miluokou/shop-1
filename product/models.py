# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

# 商品属性表
class ProductSkus(models.Model):
    title = models.CharField(max_length=255,verbose_name='SKU 名称')
    product = models.ForeignKey('Products', models.DO_NOTHING, verbose_name='所属商品 id')
    price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='SKU 价格')
    stock = models.PositiveIntegerField(verbose_name='库存')
    created_at = models.DateTimeField(blank=True, null=True,verbose_name='创建时间')
    updated_at = models.DateTimeField(blank=True, null=True,verbose_name='更新时间')

    class Meta:
        db_table = 'product_skus'
        # 模型在后台的名称
        verbose_name = "商品SKU"
        verbose_name_plural = verbose_name

# 商品表
class Products(models.Model):
    title = models.CharField(max_length=255,verbose_name="商品名称")
    description = models.TextField(verbose_name="商品详情")
    image = models.CharField(max_length=255,verbose_name='商品封面图片文件路径')
    on_sale = models.IntegerField(verbose_name='商品是否正在售卖')
    sold_count = models.PositiveIntegerField(verbose_name='销量')
    review_count = models.PositiveIntegerField(verbose_name='评价数量')
    rating = models.FloatField(verbose_name='商品平均评分')
    price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='SKU 最低价格')
    created_at = models.DateTimeField(blank=True, null=True,verbose_name='创建时间')
    updated_at = models.DateTimeField(blank=True, null=True,verbose_name='更新时间')

    class Meta:
        db_table = 'products'
        # 模型在后台的名称
        verbose_name = "商品"
        verbose_name_plural = verbose_name

