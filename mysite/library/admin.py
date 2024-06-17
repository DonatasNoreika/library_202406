from django.contrib import admin
from .models import (Genre,
                     Author,
                     Book,
                     BookInstance,
                     BookReview,
                     Profile)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'display_books']

class BookInstanceInLine(admin.TabularInline):
    model = BookInstance
    extra = 0
    can_delete = False
    readonly_fields = ['uuid']
    fields = ['uuid', 'due_back', 'status']

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'isbn', 'display_genre']
    inlines = [BookInstanceInLine]

class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ['uuid', 'book', 'status', 'due_back', 'reader']
    list_filter = ['status', 'due_back']
    search_fields = ['uuid', 'book__title', 'book__author__first_name', 'book__author__last_name']
    list_editable = ['status', 'due_back', 'reader']

    fieldsets = (
        ("Pagrindinis", {'fields': ('uuid', 'book')}),
        ("Prieinamumas", {'fields': ('status', 'due_back', 'reader')}),
    )

class BookReviewAdmin(admin.ModelAdmin):
    list_display = ['book', 'reviewer', 'date_created']

# Register your models here.
admin.site.register(Genre)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
admin.site.register(BookReview, BookReviewAdmin)
admin.site.register(Profile)
