# Generated by Django 2.2.5 on 2021-04-11 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='file_url',
            field=models.URLField(blank=True, default='', null=True),
        ),
    ]
