# Generated by Django 4.2.1 on 2023-05-23 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_rename_image_product_product_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productsize',
            old_name='product',
            new_name='product_id',
        ),
    ]
