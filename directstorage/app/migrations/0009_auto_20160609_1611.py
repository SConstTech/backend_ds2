# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20160316_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientrequests',
            name='PickupDate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='clientrequests',
            name='RequestDate',
            field=models.DateField(),
        ),
    ]
