from django.apps import AppConfig
from photoHandler.model_scripts.model_global import set_model

class PhotohandlerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'photoHandler'

    def ready(self):
        import photoHandler.signals
        print("Running pre-server startup code...")
        from photoHandler.model_scripts.load_model import get_model

        print("Running pre-server startup code...")
        loaded_model = get_model()
        loaded_model.load_weights("/Users/stiks/Desktop/OpticOdesseyProject/backend/OpticOdessey/model_source/U6_E_1201-F1_0.7134-IOU_0.6555.h5")
        
        # Устанавливаем глобальную переменную модели
        set_model(loaded_model)
        
        

