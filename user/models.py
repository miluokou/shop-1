from django.db import models
from product.models import Products
# Create your models here.


#用户信息
class Users(models.Model):
    name = models.CharField(max_length=255,verbose_name='用户昵称')
    password = models.CharField(max_length=255,verbose_name='用户密码')
    email = models.CharField(unique=True, max_length=255, verbose_name='用户邮箱')
    created_at = models.DateTimeField(blank=True, null=True,verbose_name='创建时间')
    updated_at = models.DateTimeField(blank=True, null=True,verbose_name='更新时间')

    class Meta:
        db_table = 'users'
        # 模型在后台的名称
        verbose_name = "用户表"
        verbose_name_plural = verbose_name

# 用户地址
class UserAddresses(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING,verbose_name='用户ID',default='0')
    province = models.CharField(max_length=255,verbose_name='省份')
    city = models.CharField(max_length=255,verbose_name='城市')
    district = models.CharField(max_length=255,verbose_name='街道')
    address = models.CharField(max_length=255,verbose_name='具体地址')
    contact_phone = models.CharField(max_length=255,verbose_name='收货人联系方式')
    contact_name = models.CharField(max_length=255,verbose_name='收货人名字')
    created_at = models.DateTimeField(blank=True, null=True,verbose_name='创建时间')
    updated_at = models.DateTimeField(blank=True, null=True,verbose_name='更新时间')
    zip = models.CharField(max_length=255, blank=True, null=True,verbose_name='')

    class Meta:
        db_table = 'user_addresses'
        # 模型在后台的名称
        verbose_name = "用户地址表"
        verbose_name_plural = verbose_name

# 用户收藏
class UserFavoriteProducts(models.Model):
    product = models.ForeignKey(Products, models.DO_NOTHING,default='0',verbose_name='商品ID')
    user = models.ForeignKey('Users', models.DO_NOTHING,default='0',verbose_name='用户ID')
    created_at = models.DateTimeField(blank=True, null=True,verbose_name='创建时间')
    updated_at = models.DateTimeField(blank=True, null=True,verbose_name='更新时间')

    class Meta:
        db_table = 'user_favorite_products'
        # 模型在后台的名称
        verbose_name = "用户收藏表"
        verbose_name_plural = verbose_name

# 忘记密码
class PasswordResets(models.Model):
    token = models.CharField(max_length=255,verbose_name='Token')
    email = models.CharField(max_length=255,verbose_name='邮箱')
    created_at = models.DateTimeField(blank=True, null=True,verbose_name='创建时间')

    class Meta:
        db_table = 'password_resets'
        # 模型在后台的名称
        verbose_name = "忘记密码"
        verbose_name_plural = verbose_name
