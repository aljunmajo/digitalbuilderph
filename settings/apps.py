from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig

class SettingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'settings'
    verbose_name = 'Settings'
    label = 'settings'


class MyAdminConfig(AdminConfig):
    default_site = 'settings.admin.MyAdminSite'
