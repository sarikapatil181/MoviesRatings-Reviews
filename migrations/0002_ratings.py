# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MovieReviewsRatingsApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('rating_ID', models.IntegerField()),
                ('Movie_ID', models.IntegerField()),
                ('Ratings', models.FloatField()),
                ('timestamp', models.DateTimeField()),
            ],
            options={
                'db_table': 'Ratings',
            },
        ),
    ]
