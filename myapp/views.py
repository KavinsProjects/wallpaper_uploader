from django.shortcuts import render
from .forms import ImageForm
from .models import Image

def home(request):
    form = ImageForm()
    img = Image.objects.all()  # Ensure img is always defined

    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():  # Fix the typo
            form.save()  # Add parentheses to save the form

            img = Image.objects.all()  # Refresh the queryset after saving

    return render(request, 'myapp/home.html', {'img': img, 'form': form})
    