# Generated by Django 2.2.6 on 2019-10-27 15:56

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentaire',
            name='message',
            field=tinymce.models.HTMLField(verbose_name='message'),
        ),
    ]