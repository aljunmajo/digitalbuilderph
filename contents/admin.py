from django.contrib import admin

from .models import Posts, Pages, Tag, Category

class PostsAdmin(admin.ModelAdmin):
    ordering = ['-updated_at','-created']
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'created', 'updated_at']
    #list_editable = ['updated_at']
    list_per_page = 20
    search_fields = ('title', 'body')

class PagesAdmin(admin.ModelAdmin):
    ordering = ['-updated_at','-created']
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'created', 'updated_at']
    #list_editable = ['updated_at']
    list_per_page = 20
    search_fields = ('title', 'body')

class TagAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Posts, PostsAdmin)
admin.site.register(Pages, PagesAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)