# Generated by Django 5.1.1 on 2024-09-27 09:11

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_income_user_alter_cost_id_alter_income_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cost',
            name='user',
        ),
        migrations.AddField(
            model_name='cost',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name="Qo'shilgan sana"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan sana"),
        ),
    ]
