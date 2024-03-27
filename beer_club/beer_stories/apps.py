from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _ 


class BeerStoriesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'beer_stories'
    verbose_name = ('beer_stories')
