# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20150407_0753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersinfo',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
