from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Photo, Tag

# Create your views here.
def index(request):
    tag_name =request.GET.get('tag')
    if tag_name:
        photos = Photo.objects.filter(tags__name=tag_name)
    else:
        photos = Photo.objects.all().order_by('-created_at')
        tags= Tag.objects.all()
        return render(request,'index.html', {'photos': photos, 'tags': tags})
    
def register(request):
        if request.method == 'POST':
         form =UserCreationForm(request.POST)
        if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('galleryapp:index')
        else:
            form = UserCreationForm()
        return render(request, 'register.html', {'form': form})