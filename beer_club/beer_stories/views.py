from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from . import models

def index(request: HttpRequest) -> HttpResponse:
    context = {
        'types_count': models.Type.objects.count(),
        'reviews_count': models.Review.objects.count(),
        'user_count': models.get_user_model().objects.count()
    }
    return render(request, 'beer_stories/index.html', context)

def review_list(request:HttpRequest) -> HttpResponse:
    return render(request, 'beer_stories/review_list.html', {
        'review_list': models.Review.objects.all()
    })