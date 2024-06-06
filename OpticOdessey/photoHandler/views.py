from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.template.loader import render_to_string
from PIL import Image
from .forms import ImageUploadForm
from .models import UploadImage,ProcessedImage


# Home page and handler Page
def index(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            my_id = instance.my_id
            instance.save()
            image = image_processing(instance)
            return render(request, 'photoHandler/index.html', {'image':instance,'image_output': image})
    else:
        form = ImageUploadForm()
    return render(request, 'photoHandler/index.html', {'form':form})

def page_not_found(request, exception):
    return HttpResponseNotFound("<a>Not found 404</a>")


# Funcion processing image 
def image_processing(image):
    # Создаем объект ProcessedImage из изображения с измененным разрешением
    processed_image = ProcessedImage.create_from_image(image.image.path)

    return processed_image
