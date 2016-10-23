# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_clientrequests_boxid'),
    ]

    operations = [
        migrations.AddField(
            model_name='archiveunits',
            name='dateDestroyed',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='clientrequests',
            name='PickupDate',
            field=models.DateField(auto_now=True),
        ),
    ]
