# Generated by Django 3.1.4 on 2021-02-06 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_auto_20210206_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
