# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='archiveUnits',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.TextField()),
                ('comment', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='archiveUnitTypes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('active', models.BooleanField(default=True)),
                ('comment', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='boxes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('startDate', models.DateField()),
                ('expireDate', models.DateField(null=True, blank=True)),
                ('name', models.TextField(null=True, blank=True)),
                ('active', models.BooleanField(default=False)),
                ('comment', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ClientRequests',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('RequestDate', models.DateField(auto_now=True)),
                ('PickupDate', models.DateField()),
                ('AcknowledgeDate', models.DateField(null=True, blank=True)),
                ('DoneDate', models.DateField(null=True, blank=True)),
                ('boxCount', models.IntegerField(default=0)),
                ('digitalisation', models.BooleanField(default=False)),
                ('status', models.TextField()),
                ('comment', models.TextField()),
                ('clientName', models.TextField(null=True, blank=True)),
                ('projectName', models.TextField(null=True, blank=True)),
                ('archiveUnitID', models.ForeignKey(blank=True, to='app.archiveUnits', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='clients',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('bulstat', models.TextField()),
                ('mol', models.TextField()),
                ('address', models.TextField()),
                ('city', models.TextField()),
                ('postcode', models.TextField()),
                ('active', models.BooleanField(default=True)),
                ('comment', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='criteria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.TextField()),
                ('active', models.BooleanField(default=True)),
                ('comment', models.TextField()),
                ('archiveUnitID', models.ForeignKey(to='app.archiveUnits')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='criteriaTypes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('active', models.BooleanField(default=True)),
                ('comment', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='deliverTypes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('active', models.BooleanField(default=False)),
                ('comment', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fileLocation', models.ImageField(null=True, upload_to=b'scanned_images/', blank=True)),
                ('active', models.BooleanField(default=True)),
                ('comment', models.TextField(null=True, blank=True)),
            ],
            options={
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='locations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('active', models.BooleanField(default=True)),
                ('comment', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='places',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('row', models.IntegerField()),
                ('column', models.IntegerField()),
                ('position', models.IntegerField()),
                ('capacity', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
                ('comment', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='projects',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('active', models.BooleanField(default=True)),
                ('comment', models.TextField()),
                ('arhiveUnitTypeID', models.ForeignKey(to='app.archiveUnitTypes')),
                ('clientID', models.ForeignKey(to='app.clients')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='racks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('comment', models.TextField()),
                ('locationID', models.ForeignKey(to='app.locations')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='requestDatabases',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('databaseName', models.FileField(upload_to=b'documents/%y%m%d')),
                ('active', models.BooleanField(default=True)),
                ('comment', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='requestTypes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('active', models.BooleanField(default=False)),
                ('comment', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='usersInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstName', models.TextField()),
                ('middleName', models.TextField()),
                ('LastName', models.TextField()),
                ('lastName_is_familyName', models.BooleanField(default=True)),
                ('email', models.EmailField(max_length=75)),
                ('active', models.BooleanField(default=False)),
                ('comment', models.TextField()),
                ('projectID', models.ForeignKey(to='app.projects')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='places',
            name='rackID',
            field=models.ForeignKey(to='app.racks'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='criteriatypes',
            name='projectID',
            field=models.ForeignKey(to='app.projects'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='criteria',
            name='criteriaTypeID',
            field=models.ForeignKey(to='app.criteriaTypes'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clientrequests',
            name='deliverTypeID',
            field=models.ForeignKey(blank=True, to='app.deliverTypes', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clientrequests',
            name='imageID',
            field=models.ForeignKey(blank=True, to='app.Images', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clientrequests',
            name='operatorFinishID',
            field=models.ForeignKey(related_name=b'operatorFinish', default=None, blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clientrequests',
            name='operatorStartID',
            field=models.ForeignKey(related_name=b'operatorStart', default=None, blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clientrequests',
            name='requestTypeID',
            field=models.ForeignKey(blank=True, to='app.requestTypes', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clientrequests',
            name='userID',
            field=models.ForeignKey(related_name=b'user', default=None, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='boxes',
            name='databaseFileID',
            field=models.ForeignKey(blank=True, to='app.requestDatabases', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='boxes',
            name='placeID',
            field=models.ForeignKey(blank=True, to='app.places', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='boxes',
            name='projectID',
            field=models.ForeignKey(to='app.projects'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='archiveunits',
            name='boxid',
            field=models.ForeignKey(to='app.boxes'),
            preserve_default=True,
        ),
    ]
