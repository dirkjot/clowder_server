# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-27 21:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clowder_server', '0007_alert_expire_at'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='alert',
            index=models.Index(fields=['company', 'name', '-create'], name='clowder_ser_company_83dc78_idx'),
        ),
    ]