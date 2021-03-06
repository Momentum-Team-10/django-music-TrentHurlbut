# Generated by Django 3.2.9 on 2021-11-05 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='album_art_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.CharField(default=None, max_length=300),
        ),
        migrations.AddField(
            model_name='album',
            name='medium',
            field=models.CharField(choices=[('physical', 'PHYSICAL'), ('digital', 'DIGITAL')], default='digital', max_length=8),
        ),
        migrations.AddField(
            model_name='album',
            name='title',
            field=models.CharField(default=None, max_length=300),
        ),
    ]
