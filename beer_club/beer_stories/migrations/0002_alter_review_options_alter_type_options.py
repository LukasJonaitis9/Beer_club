# Generated by Django 5.0 on 2024-03-27 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beer_stories', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['rating'], 'verbose_name': 'review', 'verbose_name_plural': 'reviews'},
        ),
        migrations.AlterModelOptions(
            name='type',
            options={'ordering': ['kinds'], 'verbose_name': 'type', 'verbose_name_plural': 'types'},
        ),
    ]