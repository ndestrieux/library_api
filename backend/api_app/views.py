from rest_framework import generics

from api_app.models import Book, Album, Film
from api_app.serializers import BookSerializer, AlbumSerializer, FilmSerializer


class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "pk"


class AlbumListCreateAPIView(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class AlbumDetailUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    lookup_field = "pk"


class FilmListCreateAPIView(generics.ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


class FilmDetailUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    lookup_field = "pk"
