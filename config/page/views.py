from django.shortcuts import render, redirect, get_object_or_404
from .models import *

def home(request):
    return render(request, 'home.html')

def detail(request, song_id):
    song_detail = get_object_or_404(Song, pk=song_id)
    return render(request, 'detail.html', {'song':song_detail})

def search(request):
    songs = Song.objects.all().order_by('-id')
    q = request.POST.get('q', "")

    if q:
        songs = songs.filter(title__icontains=q)|songs.filter(genre__icontains=q)|songs.filter(artist__icontains=q)
        return render(request, 'search.html', {'songs':songs, 'q':q})

    else:
        return render(request, 'search.html')

def favorite(request):
    if not request.session.get('user'):
        return redirect('/member/login/')

    genres = ["발라드", "댄스", "R&B/Soul", "트로트", "록/메탈", "OST", "인디", "포크/블루스", "EDM", "랩/힙합"]
    return render(request, 'favorite.html', {'genres': genres})