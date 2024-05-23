from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.template.loader import render_to_string
from .forms import ImageUploadForm
from .models import UploadImage


# Home page and handler Page
def index(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            my_id = instance.my_id
            print(my_id)
            instance.save()
            return redirect('result_page', id = my_id)
    else:
        form = ImageUploadForm()
    return render(request, 'photoHandler/index.html', {'form':form})

def page_not_found(request, exception):
    return HttpResponseNotFound("<a>Not found 404</a>")

def result(request, id):
    image = get_object_or_404(UploadImage, my_id = id)
    return render(request, 'photoHandler/index.html', {'image':image})