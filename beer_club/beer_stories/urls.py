from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('type/', views.TypeListView.as_view(), name='type_list'),
    path('type/<int:pk>/', views.TypeDetailView.as_view(), name='type_detail'),
    path('type/<int:pk>/edit/', views.TypeUpdateView.as_view(), name='type_update'),
    path('review/', views.review_list, name='review_list'),
    path('review/<int:pk>/', views.review_detail, name='review_detail'),
]
