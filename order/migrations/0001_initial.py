# Generated by Django 3.0.5 on 2020-11-08 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(max_length=255, unique=True, verbose_name='订单流水号')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='订单总金额')),
                ('address', models.TextField(blank=True, null=True, verbose_name='收货地址')),
                ('remark', models.TextField(blank=True, null=True, verbose_name='订单备注')),
                ('paid_at', models.DateTimeField(blank=True, null=True, verbose_name='支付时间')),
                ('payment_method', models.CharField(blank=True, max_length=255, null=True, verbose_name='支付方式')),
                ('payment_no', models.CharField(blank=True, max_length=255, null=True, verbose_name='支付平台订单号')),
                ('coupon_code_id', models.PositiveIntegerField(blank=True, null=True, verbose_name='')),
                ('refund_status', models.CharField(max_length=255, verbose_name='退款状态')),
                ('refund_no', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='退款单号')),
                ('closed', models.IntegerField(blank=True, null=True, verbose_name='订单是否已关闭')),
                ('reviewed', models.IntegerField(blank=True, null=True, verbose_name='订单是否已评价')),
                ('extra', models.TextField(blank=True, null=True, verbose_name='其他额外的数据')),
                ('created_at', models.DateTimeField(blank=True, null=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(blank=True, null=True, verbose_name='更新时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.Users', verbose_name='下单的用户 ID')),
            ],
            options={
                'verbose_name': '订单表',
                'verbose_name_plural': '订单表',
                'db_table': 'orders',
            },
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(verbose_name='数量')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='单价')),
                ('rating', models.PositiveIntegerField(blank=True, null=True, verbose_name='用户打分')),
                ('review', models.TextField(blank=True, null=True, verbose_name='用户评价')),
                ('reviewed_at', models.DateTimeField(blank=True, null=True, verbose_name='评价时间')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='order.Orders', verbose_name='所属订单 ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.Products', verbose_name='对应商品 ID')),
                ('product_sku', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.ProductSkus', verbose_name='对应商品 SKU ID')),
            ],
            options={
                'verbose_name': '订单详情表',
                'verbose_name_plural': '订单详情表',
                'db_table': 'order_items',
            },
        ),
    ]
