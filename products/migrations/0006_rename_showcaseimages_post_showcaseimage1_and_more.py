# Generated by Django 4.1.4 on 2023-11-30 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_post_youtubeurl'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='showcaseimages',
            new_name='showcaseimage1',
        ),
        migrations.AddField(
            model_name='post',
            name='showcaseimage2',
            field=models.ImageField(default='/logo.png', upload_to='files/'),
        ),
        migrations.AddField(
            model_name='post',
            name='showcaseimage3',
            field=models.ImageField(default='/logo.png', upload_to='files/'),
        ),
        migrations.AddField(
            model_name='post',
            name='showcaseimage4',
            field=models.ImageField(default='/logo.png', upload_to='files/'),
        ),
    ]