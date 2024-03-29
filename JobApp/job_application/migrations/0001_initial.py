# Generated by Django 5.0.2 on 2024-02-18 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=240, verbose_name='Title')),
                ('responsibilities', models.CharField(max_length=1240, verbose_name='Responsibilities')),
                ('requirements', models.CharField(max_length=1240, verbose_name='Requirements')),
                ('link', models.URLField(max_length=250, verbose_name='Link')),
            ],
        ),
    ]
