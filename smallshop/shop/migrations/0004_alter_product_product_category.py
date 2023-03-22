# Generated by Django 4.1 on 2023-03-14 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_product_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='cat_name', to='shop.category'),
        ),
    ]
