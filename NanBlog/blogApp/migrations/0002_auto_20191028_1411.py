# Generated by Django 2.2.6 on 2019-10-28 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentaire',
            name='email',
        ),
        migrations.RemoveField(
            model_name='commentaire',
            name='nom',
        ),
    ]
