from django.conf import settings
from django.db import models

from contents.models import Pages, Posts


class GeneralSettings(models.Model):
    settings_title = models.CharField(max_length=300, null=True, blank=True)
    site_title = models.CharField(max_length=300, null=True, blank=True)
    tagline = models.CharField(max_length=300, default="Another Django Website")
    site_url = models.CharField(max_length=300, blank=True, null=True)
    admininstration_email = models.EmailField(max_length=300, blank=True, null=True)#This address is used for admin purposes. If you change this, we will send you an email at your new address to confirm it. The new address will not become active until confirmed.
    membership = models.BooleanField(default=False, help_text="anyone can reigister?")#anyone can reigister? 
    site_language = models.ForeignKey('SiteLanguage', on_delete=models.SET_NULL, null=True, blank=True, related_name="st")#dropdown
    timezone =   models.ForeignKey('TimeZone', on_delete=models.SET_NULL, null=True, blank=True, related_name="tz")#dropdown 
    search_engine_visibility = models.BooleanField(
        default=False, 
        verbose_name="Search engine visibility",
        help_text="Discourage search engines from indexing this site",
        )#Discourage search engines from indexing this site

class ReadingSettings(models.Model):
    settings_title = models.CharField(max_length=300, null=True, blank=True)
    home_display = models.ManyToManyField(Pages, blank=True)
    blog_display = models.ManyToManyField(Posts, blank=True)
    blog_posts_show = models.IntegerField(default=10, null=True, blank=True)#Blog pages show at most

class SiteLanguage(models.Model):
    language = models.CharField(max_length=50)

    def __str__(self):
        return self.language

class TimeZone(models.Model):
    timezone = models.CharField(max_length=50)

    def __str__(self):
        return self.timezone