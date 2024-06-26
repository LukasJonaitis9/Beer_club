from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('detail/', views.user_detail, name='user_detail_current'),
    path('detail/<str:username>/', views.user_detail, name='userdetail'),
    path('user/<str:username>/', views.user_detail, name='user_detail'),
    path('esit/', views.user_update, name='user_update'),
]
