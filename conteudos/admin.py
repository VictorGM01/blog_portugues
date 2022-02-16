from django.contrib import admin
from .models import Post


@admin.register(Post)
class ListaPost(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'data_postagem']
    list_display_links = ['id', 'titulo']
