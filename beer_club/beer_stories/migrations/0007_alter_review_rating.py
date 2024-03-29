# Generated by Django 5.0 on 2024-03-28 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beer_stories', '0006_alter_review_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.CharField(choices=[('1 out of 5', 'very bad'), ('2 out of 5', 'bad'), ('3 out of 5', 'average'), ('4 out of 5', 'good'), ('5 out of 5', 'perfect')], help_text='Choose beer rating', max_length=10),
        ),
    ]
