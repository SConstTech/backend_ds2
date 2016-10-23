# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20151112_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='fileLocation',
            field=models.FileField(null=True, upload_to=b'scanned_images', blank=True),
        ),
    ]
