from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug')
    search_fields = ['title']
    list_filter = ['created_at']
    class Meta:
        model = Post