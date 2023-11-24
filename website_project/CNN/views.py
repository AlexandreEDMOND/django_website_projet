from django.shortcuts import render, redirect
from .forms import ImageUploadForm

def page_cnn(request):
    return render(request, 'page_cnn.html')

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirigez vers la page d'accueil ou toute autre page souhaitée après le téléchargement.
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})