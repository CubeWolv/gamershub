# Generated by Django 4.1.4 on 2023-11-24 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='product_type',
            field=models.CharField(choices=[('top_sellers', 'Top Sellers'), ('new_releases', 'New Releases'), ('old_releases', 'Old Releases'), ('top', 'Top'), ('Event', 'Event')], max_length=20),
        ),
    ]
