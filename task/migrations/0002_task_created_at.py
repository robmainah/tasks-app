# Generated by Django 4.1.6 on 2023-02-10 07:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 10, 7, 12, 59, 740565, tzinfo=datetime.timezone.utc)),
        ),
    ]