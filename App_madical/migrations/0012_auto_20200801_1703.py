# Generated by Django 2.2.11 on 2020-08-01 17:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_madical', '0011_auto_20200801_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instock',
            name='N_data',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 8, 1, 17, 3, 10, 763483), null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='M_date',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 8, 1, 17, 3, 10, 763019), null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='gst_number',
            field=models.TextField(blank=True, null=True),
        ),
    ]
