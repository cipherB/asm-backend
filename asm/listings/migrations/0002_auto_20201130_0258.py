# Generated by Django 3.1.3 on 2020-11-30 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='image',
            field=models.ImageField(upload_to='photos/anime/'),
        ),
        migrations.AlterField(
            model_name='movies',
            name='image',
            field=models.ImageField(upload_to='photos/movies/'),
        ),
        migrations.AlterField(
            model_name='series',
            name='image',
            field=models.ImageField(upload_to='photos/series/'),
        ),
    ]
