from django.contrib import admin
from .models import Genre, Author, Book, BookInstance

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'isbn', 'display_genre']


class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ['uuid', 'book', 'status', 'due_back']
    list_filter = ['status', 'due_back']

    fieldsets = (
        ("Pagrindinis", {'fields': ('uuid', 'book')}),
        ("Prieinamumas", {'fields': ('status', 'due_back')}),
    )

# Register your models here.
admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Book, BookAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
