# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField()),
                ('release_year', models.IntegerField()),
                ('locations', models.TextField()),
                ('production_company', models.TextField()),
                ('director', models.TextField()),
                ('writer', models.TextField()),
                ('actor_1', models.TextField()),
                ('actor_2', models.TextField()),
                ('actor_3', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
