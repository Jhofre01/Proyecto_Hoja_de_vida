from django.apps import AppConfig


class PaginasusuarioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'paginasusuario'

    def ready(self):
        import paginasusuario.signals

