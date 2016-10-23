# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20160609_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criteria',
            name='archiveUnitID',
            field=models.ForeignKey(related_name='units', to='app.archiveUnits'),
        ),
    ]
