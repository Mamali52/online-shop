# Generated by Django 5.0.6 on 2024-06-25 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='recommend',
        ),
    ]
