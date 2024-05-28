# signals.py

from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import UploadImage, ProcessedImage

@receiver(post_delete, sender=UploadImage)
def delete_file_on_instance_delete(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(False)

@receiver(post_delete, sender=ProcessedImage)
def delete_file_on_instance_delete(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(False)