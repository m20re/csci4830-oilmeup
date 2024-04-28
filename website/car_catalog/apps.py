from django.apps import AppConfig


class CarCatalogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'car_catalog'
    def ready(self):
        import car_catalog.signals