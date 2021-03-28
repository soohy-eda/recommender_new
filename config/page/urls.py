from django.urls import path
from . import views

urlpatterns = [
    path('favorite/', views.favorite, name='favorite'),
    path('search/', views.search, name='search'),
    path('detail/<int:song_id>', views.detail, name='detail'),
]
