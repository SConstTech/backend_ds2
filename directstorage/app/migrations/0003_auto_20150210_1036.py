# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_clientrequests_imagehash'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='arhiveUnitTypeID',
            new_name='archiveUnitTypeID',
        ),
        migrations.AlterField(
            model_name='clients',
            name='bulstat',
            field=models.TextField(unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='images',
            name='fileLocation',
            field=models.ImageField(null=True, upload_to=b'scanned_images', blank=True),
            preserve_default=True,
        ),
    ]
