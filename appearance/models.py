from django.db import models
from contents.models import Pages

#TODOS: create drag and dropb func.
class Menus(models.Model):
    MENU_LOCATION = (
        ("page-menu", "Page Menu"),
        ("sidebar-menu", "Sidebar Menu"),
        ("footer-menu", "Footer Menu"),
        ("social-media-menu", "Social Media Menu"),
    )


    menu_name = models.CharField(max_length=300)
    #menu_links = models.ForeignKey(Pages, on_delete=models.CASCADE, null=True, blank=True)
    menu_links = models.ManyToManyField(Pages, blank=True)
    display_location = models.CharField(max_length=20, choices=MENU_LOCATION)
    menu_notes = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menus"

    def __str__(self):
        return self.menu_name