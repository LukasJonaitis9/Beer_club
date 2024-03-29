from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.contrib import messages
from . import models, forms
from django.db.models import Count


#
class TypeListView(generic.ListView):
    model = models.Type
    template_name = 'beer_stories/type_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.annotate(review_count=Count('review'))
        return queryset
#

class TypeDetailView(generic.DetailView):
    model = models.Type
    template_name = 'beer_stories/type_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        type_obj = self.get_object()
        context['reviews'] = type_obj.review.all()  # Use the related name 'review'
        return context


class TypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = models.Type
    template_name = 'beer_stories/type_create.html'
    fields = ('name')

    def get_success_url(self) -> str:
        messages.success(self.request,
        ('type created succesfully').capitalize())
    
    def from_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
#UPDEITAI UZKOMENTUOTI??????????????
    
class TypeUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = models.Type
    template_name = 'beer_stories/type_update.html'
    fields=('name')

    def get_success_url(self) -> str:
        messages.success(self.request,
        ('type updated succesfully').capitalize())

    def test_func(self) -> bool | None:
        return self.get_object().owner == self.request.user


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

def review_detail(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'beer_stories/review_detail.html', {
        'review': get_object_or_404(models.Review, pk=pk),
    })

@login_required
def review_create(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = forms.ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.owner = request.user
            review.save()
            messages.success(request, 'Review created successfully'.capitalize())
            return redirect('review_list')
    else:
        form = forms.ReviewForm()
    return render(request, 'beer_stories/review_create.html', {'form': form})

@login_required
def review_like(request: HttpRequest, pk: int) -> HttpResponse:
    review = get_object_or_404(models.Review, pk=pk)
    like = models.ReviewLike.objects.filter(review=review, user=request.user).first()
    if not like:
        models.ReviewLike.objects.create(review=review, user=request.user)
    else:
        like.delete()
    if request.GET.get('next'):
        return redirect(request.GET.get('next'))
    return redirect('review_list')