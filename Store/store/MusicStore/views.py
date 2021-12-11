from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Albums

# Create your views here.
def index(request):
    context = {'albums': Albums.objects.order_by('-id')[::-1]}
    return render(request, 'MusicStore/index.html', context)

def detail(request, album_id):
    album = get_object_or_404(Albums, pk=album_id)
    songs = album.songs_set.all()
    return render(request, 'MusicStore/detail.html', {'album': album, 'songs': songs})

def edit(request, album_id):
    album = get_object_or_404(Albums, pk=album_id)
    songs = album.songs_set.all()
    return render(request, 'MusicStore/edit.html', {'album': album, 'songs': songs})

def editsave(request, album_id):
    album = get_object_or_404(Albums, pk=album_id)
    songs = album.songs_set.all()
    album.title = request.POST['album-title-form']
    album.description = request.POST['album-description-form']
    for song in songs:
        song.title = request.POST[f'song-title-form-{song.id}']
        song.link = request.POST[f'song-link-form-{song.id}']
        song.save()
    album.save()
    return HttpResponseRedirect(reverse('MusicStore:detail', args=(album.id,)))

def search(request):
    if request.method == "GET":
        search = request.GET.get('search').title()
        albums = Albums.objects.all().filter(title__contains=search)
        return render(request, 'MusicStore/index.html', {'albums': albums})