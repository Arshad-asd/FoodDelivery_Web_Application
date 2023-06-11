# Generated by Django 4.2.1 on 2023-06-10 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_remove_profileaddress_profile_pic_profilepic'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='checkout_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Out for Shipping', 'Out for Shipping'), ('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled'), ('Out for Delivery', 'Out for Delivery'), ('Delivered', 'Delivered')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productsize',
            name='offer_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Processing', 'Processing'), ('Completed', 'Completed'), ('Failed', 'Failed')], max_length=50),
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('order_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.product')),
            ],
        ),
    ]