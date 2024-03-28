# Generated by Django 5.0 on 2024-03-28 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beer_stories', '0004_alter_review_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='filtered',
            field=models.CharField(blank=True, choices=[('Filtered', 'Filtered'), ('Unfiltered', 'Unfiltered')], help_text='Choose filtered or unfiltered beer!', max_length=20, null=True),
        ),
    ]
