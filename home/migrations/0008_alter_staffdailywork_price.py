# Generated by Django 5.1.1 on 2024-10-23 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_staffdailywork_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffdailywork',
            name='price',
            field=models.FloatField(verbose_name='Narx'),
        ),
    ]
