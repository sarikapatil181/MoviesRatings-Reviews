# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('Movie_ID', models.IntegerField()),
                ('Movie_Name', models.CharField(max_length=100)),
                ('Genres', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Movies',
            },
        ),
    ]
