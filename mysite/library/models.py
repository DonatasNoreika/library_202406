from django.db import models
import uuid
from django.contrib.auth.models import User
from datetime import date
from tinymce.models import HTMLField


# Create your models here.
class Genre(models.Model):
    name = models.CharField(verbose_name="Pavadinimas", max_length=200,
                            help_text='Įveskite knygos žanrą (pvz. detektyvas)')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Žanras"
        verbose_name_plural = "Žanrai"


class Author(models.Model):
    first_name = models.CharField(verbose_name="Vardas", max_length=100)
    last_name = models.CharField(verbose_name="Pavardė", max_length=100)
    description = HTMLField(verbose_name="Aprašymas", max_length=3000, default="")

    def display_books(self):
        return ", ".join(book.title for book in self.books.all())

    display_books.short_description = "Knygos"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Autorius"
        verbose_name_plural = "Autoriai"


class Book(models.Model):
    title = models.CharField(verbose_name="Pavadinimas", max_length=200)
    summary = models.TextField(verbose_name="Aprašymas", max_length=1000)
    isbn = models.CharField(verbose_name="ISBN", max_length=13,
                            help_text='13 Simbolių <a href="https://www.isbn-international.org/content/what-isbn">ISBN kodas</a>')
    author = models.ForeignKey(to='Author', verbose_name="Autorius", on_delete=models.SET_NULL, null=True, blank=True,
                               related_name='books')
    genre = models.ManyToManyField(to="Genre", verbose_name="Žanrai", help_text='Išrinkite žanrą(us) šiai knygai')
    cover = models.ImageField(verbose_name="Viršelis", upload_to="covers", null=True, blank=True)

    def display_genre(self):
        genres = self.genre.all()
        names = list(genre.name for genre in genres)
        result = ", ".join(names)
        return result

    display_genre.short_description = 'Žanras'

    def __str__(self):
        return f"{self.title} ({self.author})"

    class Meta:
        verbose_name = "Knyga"
        verbose_name_plural = "Knygos"


class BookInstance(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, help_text='Unikalus ID knygos kopijai')
    book = models.ForeignKey(to="Book", verbose_name="Knyga", on_delete=models.SET_NULL, null=True, blank=True,
                             related_name="instances")
    due_back = models.DateField(verbose_name="Bus prieinama", null=True, blank=True)
    reader = models.ForeignKey(to=User, verbose_name="Skaitytojas", on_delete=models.SET_NULL, null=True, blank=True)

    LOAN_STATUS = (
        ('a', 'Administruojama'),
        ('p', 'Paimta'),
        ('g', 'Galima paimti'),
        ('r', 'Rezervuota'),
    )

    status = models.CharField(verbose_name="Būsena", max_length=1, choices=LOAN_STATUS, null=True, blank=True,
                              default='a', help_text='Statusas')

    def is_overdue(self):
        return self.due_back and (self.due_back < date.today())

    def __str__(self):
        return f"{self.book} ({self.uuid}) - {self.get_status_display()} ({self.due_back})"

    class Meta:
        verbose_name = "Egzempliorius"
        verbose_name_plural = "Egzemplioriai"


class BookReview(models.Model):
    book = models.ForeignKey(to="Book", verbose_name="Knyga", on_delete=models.SET_NULL, null=True, blank=True,
                             related_name="reviews")
    reviewer = models.ForeignKey(to=User, verbose_name="Komentatorius", on_delete=models.SET_NULL, null=True,
                                 blank=True)
    date_created = models.DateTimeField(verbose_name="Data", auto_now_add=True)
    content = models.TextField(verbose_name="Atsiliepimas", max_length=2000)

    class Meta:
        verbose_name = "Atsiliepimas"
        verbose_name_plural = "Atsiliepimai"
        ordering = ['-date_created']


class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    photo = models.ImageField(verbose_name="photo", default="profile_pics/default.png", upload_to="profile_pics")

    def __str__(self):
        return f"{self.user.username} profilis"
