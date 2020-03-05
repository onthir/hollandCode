# Generated by Django 2.1.5 on 2020-03-03 15:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=500, null=True)),
                ('email', models.CharField(max_length=500)),
                ('rScore', models.IntegerField()),
                ('iScore', models.IntegerField()),
                ('aScore', models.IntegerField()),
                ('sScore', models.IntegerField()),
                ('eScore', models.IntegerField()),
                ('cScore', models.IntegerField()),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
