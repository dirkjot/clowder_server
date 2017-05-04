# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 18:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clowder_account', '0005_company_name'),
        ('clowder_server', '0005_auto_20170503_0031'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='alert',
            unique_together=set([('company', 'name')]),
        ),
        migrations.AlterIndexTogether(
            name='alert',
            index_together=set([]),
        ),
    ]