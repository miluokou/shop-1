from django.db import models
from product.models import Products
# Create your models here.


#用户信息
class Users(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'

# 用户地址
class UserAddresses(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    province = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255)
    contact_phone = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    zip = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_addresses'


# 用户收藏
class UserFavoriteProducts(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    product = models.ForeignKey(Products, models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_favorite_products'


# 忘记密码
class PasswordResets(models.Model):
    email = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'password_resets'
