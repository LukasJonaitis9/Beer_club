from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse

class Type(models.Model):
    name = models.CharField(_("name"), max_length=50, db_index=True)
    owner = models.ForeignKey(
        get_user_model(),
        verbose_name=_("owner"),
        on_delete=models.CASCADE,
        related_name = 'types'
        )
    MAIN_KINDS = (
        ('Wheat beer', 'Wheat beer'),
        ('Pilsner', 'Pilsner'),
        ('IPA', 'IPA'),
        ('ALE', 'ALE'),
        ('Stout', 'Stout'),
        ('Bock', 'Bock'),
        ('Lager', 'Lager'),
        )
    kinds = models.CharField(max_length=10,                          
        choices=MAIN_KINDS, null=True, blank=True,
        help_text='Chose your type of beer!'
        )
    
    class Meta:
        verbose_name = _("type")
        verbose_name_plural = _("types")
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("type_detail", kwargs={"pk": self.pk})
    

class Review(models.Model):
    name = models.CharField(_("name"), max_length=100, db_index=True, help_text='Enter beer name')
    description = models.TextField(_("description"), blank=True, max_length=10000)
    image = models.URLField(max_length=2000, help_text='Enter URL for beer image', blank=True, default='')
    type = models.ForeignKey(
        Type,
        on_delete=models.CASCADE, 
        verbose_name=_("type"), 
        related_name='review',
    )

    RATINGS = (
        ('1', 'very bad'),
        ('2', 'bad'),
        ('3', 'average'),
        ('4', 'good'),
        ('5', 'perfect')
    )
    
    rating = models.CharField(max_length=1, choices=RATINGS, help_text='Choose beer rating')

    COLOR_TYPES = (
        ('Light / Straw', 'Light / Straw'),
        ('Amber', 'Amber'),
        ('Copper / Reddish-Brown', 'Copper / Reddish-Brown'),
        ('Brown', 'Brown'),
        ('Black', 'Black'),
    )

    color = models.CharField(max_length=22, choices=COLOR_TYPES, help_text='Choose your colour of beer!')

    FILTERED = (
        ('y', 'Filtered'),
        ('n', 'Unfiltered')
    )

    filtered = models.CharField(max_length=20, choices=FILTERED, null=True, blank=True, help_text='Choose filtered or unfiltered beer!')
    
    date = models.DateField(auto_now_add=True)

    
    class Meta:
        verbose_name = _("review")
        verbose_name_plural = _("reviews")
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("review_detail", kwargs={"pk": self.pk})
    
