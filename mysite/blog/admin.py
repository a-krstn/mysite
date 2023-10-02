from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']     # список полей, которые отображаются в админке
    list_filter = ['status', 'created', 'publish', 'author']            # список полей, по которым можно фильтровать посты
    search_fields = ['title', 'body']                                   # список полей, по которым можно выполнять поиск
    prepopulated_fields = {'slug': ('title',)}                          # предварительно заполняющиеся поля
    raw_id_fields = ['author']                                          # поле, отображающееся поисковым виджетом
    date_hierarchy = 'publish'                                          # поле, по которому формируются навигационные ссылки
    ordering = ['status', 'publish']                                    # критерии сортировки по умолчанию
