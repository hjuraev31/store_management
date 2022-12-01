from django.apps import AppConfig


class SkladCoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sklad_core'

    def ready(self) -> None:
        from jobs import updater
        updater.startCron()