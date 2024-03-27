# Generated by Django 5.0 on 2024-03-27 10:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, verbose_name='name')),
                ('kinds', models.CharField(blank=True, choices=[('Wheat beer', 'Wheat beer'), ('Pilsner', 'Pilsner'), ('IPA', 'IPA'), ('ALE', 'ALE'), ('Stout', 'Stout'), ('Bock', 'Bock'), ('Lager', 'Lager')], help_text='Chose your type of beer!', max_length=10, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='types', to=settings.AUTH_USER_MODEL, verbose_name='owner')),
            ],
            options={
                'verbose_name': 'type',
                'verbose_name_plural': 'types',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, help_text='Enter beer name', max_length=100, verbose_name='name')),
                ('description', models.TextField(blank=True, max_length=10000, verbose_name='description')),
                ('image', models.URLField(blank=True, default='', help_text='Enter URL for beer image', max_length=2000)),
                ('rating', models.CharField(choices=[('1', 'very bad'), ('2', 'bad'), ('3', 'average'), ('4', 'good'), ('5', 'perfect')], help_text='Choose beer rating', max_length=1)),
                ('color', models.CharField(choices=[('Light / Straw', 'Light / Straw'), ('Amber', 'Amber'), ('Copper / Reddish-Brown', 'Copper / Reddish-Brown'), ('Brown', 'Brown'), ('Black', 'Black')], help_text='Choose your colour of beer!', max_length=22)),
                ('filtered', models.CharField(blank=True, choices=[('y', 'Filtered'), ('n', 'Unfiltered')], help_text='Choose filtered or unfiltered beer!', max_length=20, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='beer_stories.type', verbose_name='type')),
            ],
            options={
                'verbose_name': 'review',
                'verbose_name_plural': 'reviews',
            },
        ),
    ]