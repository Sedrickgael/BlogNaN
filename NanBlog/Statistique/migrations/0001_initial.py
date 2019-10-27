# Generated by Django 2.2.6 on 2019-10-27 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField()),
                ('continent', models.CharField(max_length=160)),
                ('pays', models.CharField(max_length=160)),
                ('ville', models.CharField(max_length=160)),
                ('reseau', models.CharField(max_length=160)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('page', models.CharField(max_length=160)),
                ('date_visite', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
            },
        ),
    ]
