# Generated by Django 5.1.1 on 2024-10-23 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_user_managers_remove_user_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staffdailywork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Xarajat nomi')),
                ('price', models.BigIntegerField(verbose_name='Narx')),
            ],
            options={
                'db_table': 'staffdailywork',
            },
        ),
    ]
