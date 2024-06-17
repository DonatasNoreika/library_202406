from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("authors/", views.authors, name="authors"),
    path("authors/<int:author_id>", views.author, name="author"),
    path("books/", views.BookListView.as_view(), name="books"),
    path("books/<int:pk>", views.BookDetailView.as_view(), name="book"),
    path("search/", views.search, name='search'),
    path("myinstances/", views.MyBookInstanceListView.as_view(), name="my_instances"),
    path("register/", views.register, name='register'),
    path("profile/", views.profile, name="profile"),
]