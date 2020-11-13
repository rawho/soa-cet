from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'), 
    path('artist/<str:pk>/<str:slug>/', views.artist_detail, name='artist_detail')
]