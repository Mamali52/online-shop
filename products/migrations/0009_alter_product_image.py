# Generated by Django 5.0.6 on 2024-07-07 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_product_image_alter_comment_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='product/product_cover/', verbose_name='Product Image'),
        ),
    ]
