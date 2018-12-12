# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-11-09 18:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('civictechprojects', '0017_auto_20181030_0338'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteerrelation',
            name='projected_end_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='volunteerrelation',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='volunteer_relations', to='civictechprojects.Project'),
        ),
        migrations.AlterField(
            model_name='volunteerrelation',
            name='volunteer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='volunteer_relations', to='democracylab.Contributor'),
        ),
    ]
