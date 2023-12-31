# Generated by Django 4.1.4 on 2023-11-29 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_post_product_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='aboutgame',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='post',
            name='developer',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='post',
            name='genre',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='post',
            name='language',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='post',
            name='platform',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='post',
            name='publisher',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='post',
            name='releasedate',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='post',
            name='showcaseimages',
            field=models.ImageField(default='/logo.png', upload_to='files/'),
        ),
        migrations.AddField(
            model_name='post',
            name='youtubeurl',
            field=models.URLField(default=''),
        ),
    ]
