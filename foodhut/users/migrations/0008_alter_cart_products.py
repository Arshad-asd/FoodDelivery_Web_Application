# Generated by Django 4.2.1 on 2023-05-31 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_cart_cartitem_cart_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(through='users.CartItem', to='users.product'),
        ),
    ]
