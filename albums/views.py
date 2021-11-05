from django.shortcuts import render
from .models import Album
from django.utils import timezone

def post_collection(request):
    albums = Album.objects.all()
    return render(request, 'albums/album_collection.html', {'albums':albums})
