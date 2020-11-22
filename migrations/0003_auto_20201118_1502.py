# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MovieReviewsRatingsApp', '0002_ratings'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('review_ID', models.IntegerField()),
                ('Movie_ID', models.IntegerField()),
                ('Review', models.TextField(max_length=1000)),
                ('timestamp', models.DateTimeField()),
            ],
            options={
                'db_table': 'Review',
            },
        ),
        migrations.RenameField(
            model_name='ratings',
            old_name='Ratings',
            new_name='Rating',
        ),
        migrations.AlterModelTable(
            name='ratings',
            table='Rating',
        ),
    ]
