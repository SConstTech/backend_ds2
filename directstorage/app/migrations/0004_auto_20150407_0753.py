# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20150210_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersinfo',
            name='projectID',
            field=models.ForeignKey(blank=True, to='app.projects', null=True),
            preserve_default=True,
        ),
    ]
