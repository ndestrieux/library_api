from rest_framework.response import Response
from rest_framework import status
# from rest_framework.decorators import api_view
# from django.forms.models import model_to_dict
from rest_framework import generics

from api_app.models import Book
from api_app.serializers import BookSerializer


# Books views
class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailAPIView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'
