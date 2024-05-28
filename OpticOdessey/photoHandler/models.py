from django.db import models
import uuid
from io import BytesIO
from PIL import Image
from django.core.files import File
from django.core.files.base import ContentFile

# Create your models here.
class UploadImage(models.Model):
    image = models.ImageField(upload_to='uploads_images/')
    uploaded_at =  models.DateTimeField(auto_now=True)
    my_id = models.UUIDField(default=uuid.uuid4, editable=False)  # Дополнительное поле с уникальным идентификатором



class ProcessedImage(models.Model):
    image = models.ImageField(upload_to='processed_images/')
    uploaded_at =  models.DateTimeField(auto_now=True)
    my_id = models.UUIDField(default=uuid.uuid4, editable=False)
    @classmethod
    def create_from_image(cls, img, new_width, new_height):
        processed_image = cls()
        image = Image.open(img)
        # Изменяем размер изображения
        img_resized = image.resize((new_width, new_height))
        
        # Сохраняем изображение в памяти
        buffer = BytesIO()
        img_resized.save(buffer, format='JPEG')
        buffer.seek(0)
        
        # Сохраняем изображение в поле ImageField
        processed_image.image.save('image.jpg', ContentFile(buffer.read()))
        
        return processed_image  