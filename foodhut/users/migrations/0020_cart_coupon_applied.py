# Generated by Django 4.2.1 on 2023-07-04 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_coupon_min_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='coupon_applied',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.coupon'),
        ),
    ]
