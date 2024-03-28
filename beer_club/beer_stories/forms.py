from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('name', 'type', 'rating', 'color', 'filtered', 'description', 'image')