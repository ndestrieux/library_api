from django.db import models
from django.utils.translation import gettext_lazy as _


class Publisher(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=128)
    publication_year = models.IntegerField(null=True, blank=True)
    publisher = models.ForeignKey(
        Publisher, blank=True, null=True, on_delete=models.SET_NULL
    )

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    books = models.ManyToManyField(Book)

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Album(models.Model):
    class Format(models.TextChoices):
        UNKNOWN = "unknown", _("Unknown")
        CD = "cd", _("CD")
        VINYL = "vinyl", _("Vinyl")

    title = models.CharField(max_length=128)
    performer = models.ForeignKey(
        Artist,
        related_name="performer",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    composer = models.ForeignKey(
        Artist,
        related_name="composer",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    release_year = models.IntegerField(null=True, blank=True)
    genre = models.CharField(max_length=64, null=True, blank=True)
    format = models.CharField(
        max_length=10, choices=Format.choices, default=Format.UNKNOWN
    )

    class Meta:
        ordering = ["performer"]


class Film(models.Model):
    title = models.CharField(max_length=128)
    release_year = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class FilmDirector(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    films = models.ManyToManyField(Film)

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.name
