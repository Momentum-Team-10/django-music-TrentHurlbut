from django.shortcuts import render
from .models import Album
from django.utils import timezone
from .forms import AlbumForm
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404

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

def view_album(request, pk):
  album = get_object_or_404(Album, pk = pk)
  if request.method == 'POST':
    if "edit_album_button" in request.POST:
      form = AlbumForm(request.POST, instßance=album)
      if form.is_valid():
        form.save()
        return redirect('view_album', pk=album.pk)
    else:
      album.delete()
      return redirect('post_collection')
  else:
    if "edit_album_button" in request.GET:
      form = AlbumForm(instance=album)
      return render(request, 'blog/post_edit.html', {'form': form})
  return render(request, "albums/album_view.html", {"album": album})


"""def edit_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == "POST":
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('view_album', pk=album.pk)
    else:
        form = AlbumForm(instance=album)
    return render(request, 'blog/post_edit.html', {'form': form})"""
