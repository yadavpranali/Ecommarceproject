# Generated by Django 4.2.4 on 2023-10-06 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0004_alter_cart_pid_alter_cart_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='qty',
            field=models.IntegerField(default=1),
        ),
    ]
