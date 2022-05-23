from django.contrib import admin
from .models import GeneralSettings, ReadingSettings

from .views import SiteSettings, Test

from django.contrib import admin
from django.urls import path

class MyAdminSite(admin.AdminSite):

    def get_urls(self):
        # urlpatterns = super().get_urls()
        # urlpatterns += [
        #     path('options-general/', SiteSettings.as_view(), name='sitesettings'),
        #     path('test/', Test, name='test'),
        # ]

        #return urlpatterns

        urls = super().get_urls()
        url_patterns = [
            path('options-general/', SiteSettings.as_view(), name='sitesettings'),
            path('test/', Test, name='test'),
            ]
        return url_patterns + urls
    
        

admin.site = MyAdminSite()
#


admin.site.register(GeneralSettings)
admin.site.register(ReadingSettings)


admin.site.site_header = 'ADMIN PANEL2'
admin.site.site_title = 'SITE ADMIN2'
admin.site.index_title = 'ADMINISTRATION2'
