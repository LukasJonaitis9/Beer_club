from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('type/', views.TypeListView.as_view(), name='type_list'),
    path('type/<int:pk>/', views.TypeDetailView.as_view(), name='type_detail'),
    path('type/<int:pk>/edit/', views.TypeUpdateView.as_view(), name='type_update'),
    path('review/', views.review_list, name='review_list'),
    path('review/create/', views.review_create, name='review_create'),
    path('review/<int:pk>/', views.review_detail, name='review_detail'),
    path('review/<int:pk>/like', views.review_like, name='review_like'),
]
