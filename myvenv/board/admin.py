from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    search_fields = ['subject', 'content']
    list_display = ['subject', 'content']
    date_hierarchy = 'create_date'


admin.site.register(Post, PostAdmin)