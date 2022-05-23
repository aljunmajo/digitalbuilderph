from django.contrib import admin

from .models import Posts

class PostAdmin(admin.ModelAdmin):
    ordering = ['-updated_at','-created']
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'created', 'updated_at']
    #list_editable = ['updated_at']
    list_per_page = 20
    search_fields = ('title', 'body')



admin.site.register(Posts, PostAdmin)
