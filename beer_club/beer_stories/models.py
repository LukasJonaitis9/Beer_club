from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse
from tinymce.models import HTMLField


class Type(models.Model):
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
    
    name = models.CharField(_("name"), max_length=50, db_index=True)
    owner = models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE, 
        verbose_name=_("owner"), 
        related_name='types',
     )
    

    class Meta:
        verbose_name = _("type")
        verbose_name_plural = _("types")
        ordering = ['kinds']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("type_detail", kwargs={"pk": self.pk})
    

class Review(models.Model):
    name = models.CharField(_("name"), max_length=100, db_index=True, help_text='Enter beer name')
    
    type = models.ForeignKey(
        Type,
        on_delete=models.CASCADE, 
        verbose_name=_("type"), 
        related_name='review',
    )


    RATING = (
        ('1 out of 5', 'very bad'),
        ('2 out of 5', 'bad'),
        ('3 out of 5', 'average'),
        ('4 out of 5', 'good'),
        ('5 out of 5', 'perfect')
    )
    
    rating = models.CharField(max_length=10, choices=RATING, help_text='Choose beer rating')

    COLOR_TYPES = (
        (' Light / Straw ', ' Light / Straw '),
        (' Amber', 'Amber '),
        (' Copper / Reddish-Brown ', ' Copper / Reddish-Brown '),
        (' Brown ', ' Brown '),
        (' Black ', ' Black '),
    )

    color = models.CharField(max_length=30, choices=COLOR_TYPES, help_text='Choose your colour of beer!')

    FILTERED = (
        ('Filtered', 'Filtered'),
        ('Unfiltered', 'Unfiltered')
    )

    filtered = models.CharField(max_length=20, choices=FILTERED, null=True, blank=True, help_text='Choose filtered or unfiltered beer!')
    
    description = HTMLField(_("description"), blank=True, max_length=10000)

    image = models.URLField(max_length=2000, help_text='Enter URL for beer image', blank=True, default='')

    date = models.DateField(auto_now_add=True)

    
    class Meta:
        verbose_name = _("review")
        verbose_name_plural = _("reviews")
        ordering = ['rating']
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("review_detail", kwargs={"pk": self.pk})
    

class ReviewLike(models.Model):
    review = models.ForeignKey(
        Review, 
        verbose_name=_("review"), 
        on_delete=models.CASCADE,
        related_name='likes',
    )
    user = models.ForeignKey(
        get_user_model(), 
        verbose_name=_("user"), 
        on_delete=models.CASCADE,
        related_name='review_likes',
    )

    class Meta:
        verbose_name = _("review like")
        verbose_name_plural = _("review likes")

    def __str__(self):
        return f"{self.review} {self.user}"

    def get_absolute_url(self):
        return reverse("review_like_detail", kwargs={"pk": self.pk})