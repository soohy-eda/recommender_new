from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from member.models import Member

def home(request):
    return render(request, 'home.html')

def detail(request, song_id):
    song_detail = get_object_or_404(Song, pk=song_id)
    return render(request, 'detail.html', {'song':song_detail})

def search(request):
    songs = Song.objects.all().order_by('-title')
    q = request.POST.get('q', "")
    if q:
        songs = songs.filter(title__icontains=q)|songs.filter(artist__icontains=q)
        return render(request, 'search.html', {'songs':songs, 'q':q})

    else:
        return render(request, 'search.html')

def tags(request, tagname):
    if tagname == 1:
        songs = Song.objects.all().filter(tag='사랑').order_by('-title')[:30]
    elif tagname == 2:
        songs = Song.objects.all().filter(tag='이별').order_by('-title')[:30]
    elif tagname == 3:
        songs = Song.objects.all().filter(tag='자신감').order_by('-title')[:30]
    elif tagname == 4:
        songs = Song.objects.all().filter(tag='가족').order_by('-title')[:30]
    else:
        songs = Song.objects.all().filter(tag='위로').order_by('-title')[:30]
    context = {
        'tagname' : tagname,
        'songs' : songs
    }
    return render(request, 'tag.html', context)

def recommend(request):
    if not request.session.get('user'):
        return redirect('/member/login/')
    user = request.session.get['user']
    member = Member.objects.get(pk=user)
    songs = Song.objects.all()
    song_pre1 = songs.filter(genre=member.pregenre1)
    song_pre2 = songs.filter(genre=member.pregenre2)
    song_pre3 = songs.filter(genre=member.pregenre3)

    reco1_1 = song_pre1.filter(tag='사랑')[:10]
    reco1_2 = song_pre1.filter(tag='이별')[:10]
    reco1_3 = song_pre1.filter(tag='자신감')[:10]
    reco1_4 = song_pre1.filter(tag='가족')[:10]
    reco1_5 = song_pre1.filter(tag='위로')[:10]

    reco2_1 = song_pre2.filter(tag='사랑')[:10]
    reco2_2 = song_pre2.filter(tag='이별')[:10]
    reco2_3 = song_pre2.filter(tag='자신감')[:10]
    reco2_4 = song_pre2.filter(tag='가족')[:10]
    reco2_5 = song_pre2.filter(tag='위로')[:10]

    reco3_1 = song_pre3.filter(tag='사랑')[:10]
    reco3_2 = song_pre3.filter(tag='이별')[:10]
    reco3_3 = song_pre3.filter(tag='자신감')[:10]
    reco3_4 = song_pre3.filter(tag='가족')[:10]
    reco3_5 = song_pre3.filter(tag='위로')[:10]

    if request.method == 'GET':
        context = {
            'reco1_1': reco1_1,
            'reco1_2': reco1_2,
            'reco1_3': reco1_3,
            'reco1_4': reco1_4,
            'reco1_5': reco1_5,
            'reco2_1': reco2_1,
            'reco2_2': reco2_2,
            'reco2_3': reco2_3,
            'reco2_4': reco2_4,
            'reco2_5': reco2_5,
            'reco3_1': reco3_1,
            'reco3_2': reco3_2,
            'reco3_3': reco3_3,
            'reco3_4': reco3_4,
            'reco3_5': reco3_5,
        }
        return render(request, 'recommend.html', context)
    elif request.method == 'POST':
        return 1




