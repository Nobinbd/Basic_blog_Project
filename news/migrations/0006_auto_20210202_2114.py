# Generated by Django 3.1.4 on 2021-02-02 15:14

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0005_auto_20210202_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.contrib.auth.models.AnonymousUser, to=settings.AUTH_USER_MODEL),
        ),
    ]
