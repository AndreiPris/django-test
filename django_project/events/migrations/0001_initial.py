# Generated by Django 5.1.4 on 2024-12-07 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('slug', models.SlugField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('in_draft', models.BooleanField(default=False)),
                ('is_featured', models.BooleanField(default=False)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('location', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
                ('categories', models.JSONField(default=list)),
                ('images', models.JSONField(default=list)),
                ('coordinates', models.JSONField(blank=True, null=True)),
                ('additional_information', models.JSONField(blank=True, null=True)),
                ('followers', models.JSONField(blank=True, default=list)),
            ],
        ),
    ]
