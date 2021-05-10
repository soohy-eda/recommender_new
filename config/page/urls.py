from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('detail/<int:song_id>', views.detail, name='detail'),
    path('recommend/', views.recommend, name='recommend'),
    path('tag/<int:tagname>', views.tags, name='tag'),
]
