# Generated by Django 2.1.5 on 2020-03-06 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200305_0056'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
