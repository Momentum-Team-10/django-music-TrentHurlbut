from django.shortcuts import render
from .models import Album
from django.utils import timezone
from .forms import AlbumForm
from django.shortcuts import redirect

def post_collection(request):
    albums = Album.objects.all()
    return render(request, 'albums/album_collection.html', {'albums':albums})

def add_album(request):
  if request.method == 'POST':
    form = AlbumForm(request.POST)
    if form.is_valid():
      album = form.save(commit=False)
      album.published_date = timezone.now()
      album.save()
      return redirect('post_collection')
  else:
    form = AlbumForm()
  return render(request, 'albums/add_album.html', {'form':form})

