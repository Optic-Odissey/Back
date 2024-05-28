from django.apps import AppConfig
from photoHandler.model.load_model import get_model

class PhotohandlerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'photoHandler'

    def ready(self):
        import photoHandler.signals
        print("Running pre-server startup code...")
        model = get_model()

