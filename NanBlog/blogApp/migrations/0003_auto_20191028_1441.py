# Generated by Django 2.2.6 on 2019-10-28 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0002_auto_20191028_1411'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='like',
        ),
        migrations.AddField(
            model_name='article',
            name='is_archive',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.DeleteModel(
            name='Archive',
        ),
    ]