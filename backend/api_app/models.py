from django.db import models

# Books

class Author(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=128)
    author = models.ManyToManyField(Author)
    publication_year = models.IntegerField(null=True, blank=True)
    publisher = models.ForeignKey(Publisher, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


