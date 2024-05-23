from django.db import models
import uuid

# Create your models here.
class UploadImage(models.Model):
    image = models.ImageField(upload_to='uploads_images/', default='photoHandler/images/noimage.svg')
    uploaded_at =  models.DateTimeField(auto_now=True)
    my_id = models.UUIDField(default=uuid.uuid4, editable=False)  # Дополнительное поле с уникальным идентификатором
