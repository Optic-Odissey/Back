from django.db import models
import uuid
from photoHandler.model_scripts.deforestation_segmentaion import decode_png, predict
from photoHandler.model_scripts.model_global import get_model
from io import BytesIO
from PIL import Image
import matplotlib.pyplot as plt
import base64
import matplotlib.image
from django.core.files import File
from django.core.files.base import ContentFile


# Create your models here.
class UploadImage(models.Model):
    image = models.ImageField(upload_to='uploads_images/')
    uploaded_at =  models.DateTimeField(auto_now=True)
    my_id = models.UUIDField(default=uuid.uuid4, editable=False)  # Дополнительное поле с уникальным идентификатором



class ProcessedImage(models.Model):
    image = models.ImageField(upload_to='processed_images/')
    uploaded_at = models.DateTimeField(auto_now=True)
    my_id = models.UUIDField(default=uuid.uuid4, editable=False)
    
    @classmethod
    def create_from_image(cls, img):
        processed_image = cls()
        image = decode_png(img)

        prediction = predict(get_model(), image)
        # Сохраняем изображение в памяти
        buffer = BytesIO()
        matplotlib.image.imsave(buffer, prediction, format="png")
        buffer.seek(0)
        # Преобразование буфера в base64 для передачи в шаблон
        image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        
        processed_image.image.save('image.png', BytesIO(base64.b64decode(image_base64)), save=False)
        processed_image.save()

        return processed_image

    def save(self, *args, **kwargs):
        if not self.id:
            self.my_id = uuid.uuid4()
        super().save(*args, **kwargs)