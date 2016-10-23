# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20160609_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientrequests',
            name='PickupDate',
            field=models.DateField(null=True, blank=True),
        ),
    ]
