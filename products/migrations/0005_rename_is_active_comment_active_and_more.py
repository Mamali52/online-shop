# Generated by Django 5.0.6 on 2024-06-26 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_comment_recommend'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='is_active',
            new_name='active',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='Product',
            new_name='product',
        ),
    ]
