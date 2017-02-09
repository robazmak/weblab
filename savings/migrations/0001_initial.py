# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 03:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Savings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capital', models.DecimalField(decimal_places=2, max_digits=10)),
                ('years', models.DecimalField(decimal_places=2, max_digits=10)),
                ('interest', models.DecimalField(decimal_places=2, max_digits=10)),
                ('final_capital', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
